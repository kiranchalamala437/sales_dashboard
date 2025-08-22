import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="413437",  # MySQL password
    database="sales_dashboard"
)

# -------------------------
# 1️⃣ Total revenue per customer
# -------------------------
query1 = """
SELECT 
    c.customer_id,
    c.customer_name,
    ROUND(SUM(oi.quantity * p.price * (1 - (oi.discount_percent / 100))), 2) AS total_revenue
FROM customers c
INNER JOIN orders o ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON p.product_id = oi.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_revenue DESC;
"""
df_customers = pd.read_sql(query1, conn)
print("\n--- Total Revenue Per Customer ---")
print(df_customers)


# -------------------------
# 2️⃣ Total revenue per region
# -------------------------
query2 = """
SELECT 
    r.region_name,
    ROUND(SUM(oi.quantity * p.price * (1 - (oi.discount_percent / 100))), 2) AS total_revenue
FROM regions r
INNER JOIN customers c ON r.region_id = c.region_id
INNER JOIN orders o ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON p.product_id = oi.product_id
GROUP BY r.region_name
ORDER BY total_revenue DESC;
"""
df_regions = pd.read_sql(query2, conn)
print("\n--- Total Revenue Per Region ---")
print(df_regions)


# -------------------------
# 3️⃣ Best-selling products
# -------------------------
query3 = """
SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(SUM(oi.quantity * p.price * (1 - (oi.discount_percent / 100))), 2) AS total_revenue
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_units_sold DESC
LIMIT 10;
"""
df_products = pd.read_sql(query3, conn)
print("\n--- Top Selling Products ---")
print(df_products)


# -------------------------
# 4️⃣ Monthly sales trend
# -------------------------
query4 = """
SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    ROUND(SUM(oi.quantity * p.price), 2) AS monthly_revenue
FROM orders o
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON p.product_id = oi.product_id
GROUP BY DATE_FORMAT(o.order_date, '%Y-%m')
ORDER BY month;
"""
df_monthly = pd.read_sql(query4, conn)
print("\n--- Monthly Sales Trend ---")
print(df_monthly)


# Close the connection
conn.close()
