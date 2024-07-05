from connections.db_connection import execute_query


def insert_user(username, password, full_name, email, phone, address):
    query = """
    INSERT INTO users (username, password, full_name, email, phone, address) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (username, password, full_name, email, phone, address)
    execute_query(query, params)


def insert_admin(username, password, email):
    query = """
    INSERT INTO admins (username, password, email) 
    VALUES (%s, %s, %s)
    """
    params = (username, password, email)
    execute_query(query, params)


def insert_product(category_id, brand_id, name, description, price, stock):
    query = """
    INSERT INTO products (category_id, brand_id, name, description, price, stock) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (category_id, brand_id, name, description, price, stock)
    execute_query(query, params)


def insert_category(name, description):
    query = """
    INSERT INTO categories (name, description) 
    VALUES (%s, %s)
    """
    params = (name, description)
    execute_query(query, params)


def insert_brand(name, description):
    query = """
    INSERT INTO brands (name, description) 
    VALUES (%s, %s)
    """
    params = (name, description)
    execute_query(query, params)


def insert_order(user_id, status, total_price):
    query = """
    INSERT INTO orders (user_id, status, total_price) 
    VALUES (%s, %s, %s)
    """
    params = (user_id, status, total_price)
    execute_query(query, params)


def insert_order_detail(order_id, product_id, quantity, price):
    query = """
    INSERT INTO order_details (order_id, product_id, quantity, price) 
    VALUES (%s, %s, %s, %s)
    """
    params = (order_id, product_id, quantity, price)
    execute_query(query, params)


def insert_cart(user_id):
    query = """
    INSERT INTO cart (user_id) 
    VALUES (%s)
    """
    params = (user_id,)
    execute_query(query, params)


def insert_cart_item(cart_id, product_id, quantity):
    query = """
    INSERT INTO cart_items (cart_id, product_id, quantity) 
    VALUES (%s, %s, %s)
    """
    params = (cart_id, product_id, quantity)
    execute_query(query, params)


def insert_purchase_history(user_id, order_id):
    query = """
    INSERT INTO purchase_history (user_id, order_id) 
    VALUES (%s, %s)
    """
    params = (user_id, order_id)
    execute_query(query, params)


def insert_review(product_id, user_id, rating, comment):
    query = """
    INSERT INTO reviews (product_id, user_id, rating, comment) 
    VALUES (%s, %s, %s, %s)
    """
    params = (product_id, user_id, rating, comment)
    execute_query(query, params)


def insert_shipping_info(order_id, tracking_number, carrier, shipping_date, delivery_date):
    query = """
    INSERT INTO shipping_info (order_id, tracking_number, carrier, shipping_date, delivery_date) 
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (order_id, tracking_number, carrier, shipping_date, delivery_date)
    execute_query(query, params)


def insert_discount(product_id, discount_percentage, start_date, end_date):
    query = """
    INSERT INTO discounts (product_id, discount_percentage, start_date, end_date) 
    VALUES (%s, %s, %s, %s)
    """
    params = (product_id, discount_percentage, start_date, end_date)
    execute_query(query, params)
