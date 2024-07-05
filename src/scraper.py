import requests
from bs4 import BeautifulSoup
from connections.db_connection import execute_query, create_connection
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SCRAPINGBEE_API_KEY = '1WBNB6BCWE6XJF9RZZ1M81HIEQA3QXBBNZ3ZGTXUPVVRQ39502EEF1GJ1NSMEJ8KPC0U4IJ9AFUP4WC6'
BASE_URL = 'https://app.scrapingbee.com/api/v1/'


def scrape_products():
    url = 'https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dgaming%2Bkeyboard%26_encoding%3DUTF8%26content-id%3Damzn1.sym.12129333-2117-4490-9c17-6d31baf0582a%26pd_rd_r%3Dfa52106f-eacf-4253-b62b-7c5e16f30d89%26pd_rd_w%3DwVD3P%26pd_rd_wg%3DIpTSL%26pf_rd_p%3D12129333-2117-4490-9c17-6d31baf0582a%26pf_rd_r%3DRGWS8BYRE114RW5N2FAW%26ref%3Dpd_hp_d_atf_unk'
    endpoint = f'{BASE_URL}?url={url}&api_key={SCRAPINGBEE_API_KEY}'
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for product in soup.select('[data-component-type="s-search-result"]'):
            try:
                if (
                        product.select_one('div[data-cy="title-recipe"]') is None or
                        product.select_one('[data-cy="price-recipe"] .a-price .a-offscreen') is None
                ):
                    continue

                name = product.select_one('div[data-cy="title-recipe"]').text.strip()
                price = float(product.select_one('[data-cy="price-recipe"] .a-price .a-offscreen').text.strip().replace('$', ''))

                products.append((
                    None, None,
                    name,
                    '',
                    price,
                    1
                ))
            except AttributeError as e:
                logging.error(f"Error parsing product: {e}")

        return products

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return []
    except requests.exceptions.RequestException as err:
        logging.error(f"Other error occurred: {err}")
        return []


def get_or_create_category(product):
    category_name = product.select_one('.product-category').text.strip()
    query = "SELECT category_id FROM categories WHERE name = %s"
    category_id = fetch_one(query, (category_name,))
    if not category_id:
        insert_category_query = "INSERT INTO categories (name, description) VALUES (%s, %s)"
        execute_query(insert_category_query, (category_name, category_name))
        category_id = fetch_one(query, (category_name,))
    return category_id[0]


def get_or_create_brand(product):
    brand_name = product.select_one('.product-brand').text.strip()
    query = "SELECT brand_id FROM brands WHERE name = %s"
    brand_id = fetch_one(query, (brand_name,))
    if not brand_id:
        insert_brand_query = "INSERT INTO brands (name, description) VALUES (%s, %s)"
        execute_query(insert_brand_query, (brand_name, brand_name))
        brand_id = fetch_one(query, (brand_name,))
    return brand_id[0]


def insert_products(products):
    query = """
    INSERT INTO products (category_id, brand_id, name, description, price, stock)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    for product in products:
        try:
            execute_query(query, product)
            logging.info(f"Inserted product: {product[2]}")
        except Exception as e:
            logging.error(f"Error inserting product {product[2]}: {e}")


def fetch_one(query, params):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        result = cursor.fetchone()
        return result
    except mysql.connector.Error as err:
        logging.error(f"Error: {err}")
        return None
    finally:
        cursor.close()
        connection.close()
