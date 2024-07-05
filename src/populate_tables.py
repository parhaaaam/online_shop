from connections.db_connection import execute_query
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


def generate_fake_data():
    fake_users = []
    fake_admins = []
    fake_categories = []
    fake_brands = []
    fake_products = []
    fake_orders = []
    fake_order_details = []
    fake_cart = []
    fake_cart_items = []
    fake_purchase_history = []
    fake_reviews = []
    fake_shipping_info = []
    fake_discounts = []

    for _ in range(10):
        fake_users.append({
            'username': fake.user_name(),
            'password': fake.password(),
            'full_name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address()
        })

    for _ in range(2):
        fake_admins.append({
            'username': fake.user_name(),
            'password': fake.password(),
            'email': fake.email()
        })

    categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Toys']
    for category in categories:
        fake_categories.append({
            'name': category,
            'description': fake.text(max_nb_chars=200)
        })

    brands = ['Apple', 'Nike', 'Samsung', 'Sony', 'Amazon Basics']
    for brand in brands:
        fake_brands.append({
            'name': brand,
            'description': fake.text(max_nb_chars=200)
        })

    for _ in range(20):
        category_id = random.randint(1, len(categories))
        brand_id = random.randint(1, len(brands))
        fake_products.append({
            'category_id': category_id,
            'brand_id': brand_id,
            'name': fake.catch_phrase(),
            'description': fake.text(max_nb_chars=500),
            'price': random.uniform(10.0, 1000.0),
            'stock': random.randint(0, 100),
        })

    for _ in range(15):
        user_id = random.randint(1, 10)
        fake_orders.append({
            'user_id': user_id,
            'status': 'Pending',
            'total_price': random.uniform(50.0, 500.0),
        })

    for order_id in range(1, 16):
        products_in_order = random.sample(range(1, 21), random.randint(1, 5))
        for product_id in products_in_order:
            quantity = random.randint(1, 5)
            price = random.uniform(10.0, 500.0)
            fake_order_details.append({
                'order_id': order_id,
                'product_id': product_id,
                'quantity': quantity,
                'price': price
            })

    for _ in range(10):
        user_id = random.randint(1, 10)
        fake_cart.append({
            'user_id': user_id,
        })

    for cart_id in range(1, 11):
        products_in_cart = random.sample(range(1, 21), random.randint(1, 5))
        for product_id in products_in_cart:
            quantity = random.randint(1, 3)
            fake_cart_items.append({
                'cart_id': cart_id,
                'product_id': product_id,
                'quantity': quantity
            })

    for order_id in range(1, 16):
        user_id = random.randint(1, 10)
        fake_purchase_history.append({
            'user_id': user_id,
            'order_id': order_id,
            'purchase_date': fake.date_time_between(start_date='-1y', end_date='now')
        })

    for _ in range(50):
        product_id = random.randint(1, 20)
        user_id = random.randint(1, 10)
        fake_reviews.append({
            'product_id': product_id,
            'user_id': user_id,
            'rating': random.randint(1, 5),
            'comment': fake.text(max_nb_chars=500)
        })

    for order_id in range(1, 16):
        fake_shipping_info.append({
            'order_id': order_id,
            'tracking_number': fake.credit_card_number(card_type=None),
            'carrier': fake.company(),
            'shipping_date': fake.date_between(start_date=datetime.now() - timedelta(days=7), end_date='today'),
            'delivery_date': fake.date_between(start_date=datetime.now(), end_date=datetime.now() + timedelta(days=7))
        })

    for product_id in range(1, 21):
        fake_discounts.append({
            'product_id': product_id,
            'discount_percentage': random.uniform(5.0, 30.0),
            'start_date': fake.date_between(start_date=datetime.now(), end_date=datetime.now() + timedelta(days=365)),
            'end_date': fake.date_between(start_date=datetime.now() + timedelta(days=366), end_date=datetime.now() + timedelta(days=730))
        })

    return {
        'users': fake_users,
        'admins': fake_admins,
        'categories': fake_categories,
        'brands': fake_brands,
        'products': fake_products,
        'orders': fake_orders,
        'order_details': fake_order_details,
        'cart': fake_cart,
        'cart_items': fake_cart_items,
        'purchase_history': fake_purchase_history,
        'reviews': fake_reviews,
        'shipping_info': fake_shipping_info,
        'discounts': fake_discounts
    }


def populate_tables():
    fake_data = generate_fake_data()

    for table, data in fake_data.items():
        if data:
            columns = ', '.join(data[0].keys())  # Extract column names from keys of the first dictionary
            placeholders = ', '.join(['%s'] * len(data[0]))
            query = f"INSERT IGNORE INTO {table} ({columns}) VALUES ({placeholders})"
            params = [tuple(row.values()) for row in data]
            execute_query(query, params)



