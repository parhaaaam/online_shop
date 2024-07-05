from complex_queries import get_complex_queries
from src.create_tables import setup_database
from src.populate_tables import populate_tables
from src.scraper import scrape_products, insert_products


def main():
    setup_database()
    products = scrape_products()
    if products:
        insert_products(products)
    else:
        print("No products found to insert.")
    populate_tables()


if __name__ == '__main__':
    main()
