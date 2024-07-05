import mysql.connector
from connections import config


def create_connection():
    return mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DATABASE,
        port=config.MYSQL_PORT
    )


def create_root_connection():
    return mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        port=config.MYSQL_PORT
    )


def execute_query(query, params=None):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        if params:
            cursor.executemany(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


def fetch_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


def execute_root_query(query, params=None):
    connection = create_root_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
