import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Create SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://root:413437@localhost/sales_dashboard")

# 1. Top 5 Customers
query_customers = """
SELECT c.customer_name, 
       ROUND(SUM(oi.quantity * p.price), 2) AS total_revenue
FROM customers c
INNER JOIN orders o ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON p.product_id = oi.product_id
GROUP BY c.customer_id
ORDER BY total_revenue DESC
LIMIT 5
"""
df_customers = pd.read_sql(query_customers, engine)

# 2. Monthly Sales Trend
query_monthly = """
SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
       ROUND(SUM(oi.quantity * p.price), 2) AS total_sales
FROM orders o
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON p.product_id = oi.product_id
GROUP BY month
ORDER BY month
"""
df_monthly = pd.read_sql(query_monthly, engine)

# 3. Top 5 Products
query_products = """
SELECT p.product_name,
       ROUND(SUM(oi.quantity * p.price), 2) AS total_sales
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id
ORDER BY total_sales DESC
LIMIT 5
"""
df_products = pd.read_sql(query_products, engine)

# 4. Revenue by Region
query_regions = """
SELECT r.region_name,
       ROUND(SUM(oi.quantity * p.price), 2) AS total_sales
FROM regions r
INNER JOIN customers c ON r.region_id = c.region_id
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON p.product_id = oi.product_id
GROUP BY r.region_id
"""
df_regions = pd.read_sql(query_regions, engine)

# Close connection


# Create the plots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Top Customers
axs[0, 0].bar(df_customers['customer_name'], df_customers['total_revenue'], color='skyblue')
axs[0, 0].set_title("Top 5 Customers by Revenue")
axs[0, 0].set_ylabel("Revenue")
axs[0, 0].tick_params(axis='x', rotation=45)

# Monthly Sales
axs[0, 1].plot(df_monthly['month'], df_monthly['total_sales'], marker='o', color='green')
axs[0, 1].set_title("Monthly Sales Trend")
axs[0, 1].set_ylabel("Sales")
axs[0, 1].tick_params(axis='x', rotation=45)

# Top Products
axs[1, 0].barh(df_products['product_name'], df_products['total_sales'], color='orange')
axs[1, 0].set_title("Top 5 Products by Sales")
axs[1, 0].set_xlabel("Sales")

# Revenue by Region
axs[1, 1].pie(df_regions['total_sales'], labels=df_regions['region_name'], autopct='%1.1f%%', startangle=140)
axs[1, 1].set_title("Revenue by Region")

plt.tight_layout()
plt.show()
