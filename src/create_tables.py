from connections.db_connection import execute_query, execute_root_query, create_root_connection
from connections import config


def check_database_exists(database_name):
    query = f"SHOW DATABASES LIKE '{database_name}'"
    connection = create_root_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        connection.close()


def create_database(database_name):
    query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    execute_root_query(query)


def create_tables():
    queries = [
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            full_name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            phone VARCHAR(20),
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS admins (
            admin_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(100) UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS products (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            category_id INT,
            brand_id INT,
            name VARCHAR(1024) NOT NULL,
            description TEXT,
            price DECIMAL(10, 2) NOT NULL,
            stock INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(category_id),
            FOREIGN KEY (brand_id) REFERENCES brands(brand_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS categories (
            category_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS brands (
            brand_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            status VARCHAR(50),
            total_price DECIMAL(10, 2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS order_details (
            order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT,
            product_id INT,
            quantity INT,
            price DECIMAL(10, 2),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS cart (
            cart_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS cart_items (
            cart_item_id INT AUTO_INCREMENT PRIMARY KEY,
            cart_id INT,
            product_id INT,
            quantity INT,
            FOREIGN KEY (cart_id) REFERENCES cart(cart_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS purchase_history (
            purchase_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            order_id INT,
            purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            user_id INT,
            rating INT,
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS shipping_info (
            shipping_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT,
            tracking_number VARCHAR(100),
            carrier VARCHAR(100),
            shipping_date DATE,
            delivery_date DATE,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS discounts (
            discount_id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            discount_percentage DECIMAL(5, 2),
            start_date DATE,
            end_date DATE,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
        """
    ]

    for query in queries:
        execute_query(query)


def setup_database():
    database_name = config.MYSQL_DATABASE
    if not check_database_exists(database_name):
        create_database(database_name)
    print(f"Database '{database_name}' created successfully.")
    create_tables()
