import pandas as pd
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://root:413437@localhost/sales_dashboard")

# Example query
query_customers = """
SHOW COLUMNS from customers
"""
df_customers = pd.read_sql_query(query_customers, engine)

query_orders = """
SHOW COLUMNS from orders
"""
df_orders = pd.read_sql_query(query_orders, engine)
# Read into Pandas 
query_order_items = """
SHOW COLUMNS from order_items
"""
df_order_items = pd.read_sql_query(query_order_items, engine)

query_products = """
SHOW COLUMNS from products
"""
df_products = pd.read_sql_query(query_products, engine)

query_regions = """
SHOW COLUMNS from regions
"""
df_regions = pd.read_sql_query(query_regions, engine)

query_payment_methods = """
SHOW COLUMNS from payment_methods
"""
df_payment_methods = pd.read_sql_query(query_payment_methods, engine)

print(df_customers)
print(df_orders)
print(df_order_items)
print(df_products)
print(df_regions)
print(df_payment_methods)