from connections.db_connection import execute_query, fetch_query
from datetime import datetime, timedelta
from flask import Flask, jsonify
from connections.db_connection import execute_query
app = Flask(__name__)
# Define your queries
queries = [
    # Query 1: Count of users
    """
    SELECT COUNT(*) AS total_users FROM users
    """,

    # Query 2: Total sales amount per category
    """
    SELECT c.name AS category_name, SUM(od.price * od.quantity) AS total_sales
    FROM order_details od
    JOIN products p ON od.product_id = p.product_id
    JOIN categories c ON p.category_id = c.category_id
    GROUP BY c.name
    ORDER BY total_sales DESC
    """,

    # Query 3: List of users who placed orders in the last month
    """
    SELECT u.username, o.total_price
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    WHERE o.created_at >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
    """,

    # Query 4: Average order value
    """
    SELECT AVG(total_price) AS average_order_value
    FROM orders
    """,

    # Query 5: Products with the highest number of reviews
    """
    SELECT p.name, COUNT(r.review_id) AS review_count
    FROM products p
    LEFT JOIN reviews r ON p.product_id = r.product_id
    GROUP BY p.name
    ORDER BY review_count DESC
    LIMIT 5
    """,

    # Query 6: Top 10 users with the highest total spending
    """
    SELECT u.username, SUM(o.total_price) AS total_spent
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    GROUP BY u.username
    ORDER BY total_spent DESC
    LIMIT 10
    """,

    # Query 7: Products with discounts currently active
    """
    SELECT p.name, d.discount_percentage, d.start_date, d.end_date
    FROM products p
    JOIN discounts d ON p.product_id = d.product_id
    WHERE NOW() BETWEEN d.start_date AND d.end_date
    """,

    # Query 8: Orders with shipping info and delivery status
    """
    SELECT o.order_id, o.total_price, s.tracking_number, s.carrier, s.shipping_date, s.delivery_date
    FROM orders o
    LEFT JOIN shipping_info s ON o.order_id = s.order_id
    """,

    # Query 9: Users who have not made any purchases
    """
    SELECT u.username
    FROM users u
    LEFT JOIN orders o ON u.user_id = o.user_id
    WHERE o.order_id IS NULL
    """,

    # Query 10: Average rating per product category
    """
    SELECT c.name AS category_name, AVG(r.rating) AS average_rating
    FROM categories c
    LEFT JOIN products p ON c.category_id = p.category_id
    LEFT JOIN reviews r ON p.product_id = r.product_id
    GROUP BY c.name
    ORDER BY average_rating DESC
    """
]


# Function to execute queries and print results
@app.route('/api/complex_queries', methods=['GET'])
def get_complex_queries():
    results = []
    for query in queries:
        try:
            result = fetch_query(query)
            results.append(result)
        except Exception as e:
            results.append({"error": str(e)})
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)