# Online Shop Database and API Project

## Project Description

This project implements an online shop database system with an API for executing complex queries. The database stores information about products, customers, orders, and other relevant entities for an e-commerce platform. The API allows users to perform various complex queries on the database, providing valuable insights and data analysis capabilities.

The project utilizes:
- Python for backend logic
- Flask framework for API development
- PostgreSQL for the database
- Docker for containerization and easy deployment

## Prerequisites

- Docker and Docker Compose installed on your system
- Basic understanding of RESTful APIs and SQL queries

## Installation and Setup

1. Clone the repository:
```git clone git@github.com:parhaaaam/online_shop.git```
then
```cd online_shop```

2. Install Docker and Docker Compose:
- For Docker: Follow the official Docker installation guide for your operating system: https://docs.docker.com/get-docker/
- For Docker Compose: Follow the official Docker Compose installation guide: https://docs.docker.com/compose/install/

## Running the Application

1. Build and start the Docker containers:
```docker-compose up --build```

This command will:
- Build the Docker images for the Flask application and PostgreSQL database
- Start the containers
- Set up the database schema
- Launch the Flask API server

2. The API will be accessible at:
```http://localhost:5000/api/complex_queries```

You can now send requests to this endpoint to execute complex queries and view the results.


## ScrapeBee and Amazon API Integration
ScrapeBee is a web scraping service that allows users to easily extract data from various websites through its API. In this project, ScrapeBee is used to call the Amazon API to fetch detailed information about a gaming keyboard.

### Key Details:
- **ScrapeBee Service**: Utilized to make API calls to Amazon for data extraction.
- **Product Focus**: A specific gaming keyboard.
- **API Call Limit**: Each ScrapeBee account is limited to 1000 API calls.
- **Data Handling**: The retrieved data from Amazon is extracted and populated into the `products` table in the database.

By leveraging ScrapeBee, the project efficiently gathers necessary product information from Amazon, adhering to API call limits and ensuring the extracted data is correctly stored for further use and analysis.

## API Usage

To interact with the API and view complex query results, send a GET request to:
```http://localhost:5000/api/complex_queries```

This will return a JSON response containing the results of predefined complex queries.

## Additional Information

### Flask Framework

This project uses Flask, a lightweight WSGI web application framework in Python. Flask is known for its simplicity and flexibility, making it an excellent choice for building APIs and web applications. It provides features like routing, request handling, and easy integration with various extensions.

### Database Schema

The PostgreSQL database includes tables for:
- Products
- Customers
- Orders
- Order Items
- Categories
- Inventory

(You may want to include a brief description or diagram of your database schema here)

### Complex Queries

The API endpoint `/api/complex_queries` executes a series of predefined complex SQL queries, which may include:
- Best-selling products
- Customer purchase history
- Inventory status
- Sales trends over time

(Consider adding examples of the types of queries your API supports)

## Troubleshooting

If you encounter any issues:
1. Ensure Docker and Docker Compose are correctly installed and running.
2. Check the Docker logs for any error messages:
```docker-compose logs```
3. Verify that the PostgreSQL container is running and the database is properly initialized.
