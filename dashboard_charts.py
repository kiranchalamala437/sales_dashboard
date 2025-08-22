import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# ---------- CONFIG ----------
DB_USER = "root"
DB_PASSWORD = "413437"   # MySQL password 
DB_HOST = "localhost"
DB_NAME = "sales_dashboard"

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- CONNECT ----------
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# ---------- QUERIES ----------
queries = {
    "query1_revenue_by_customer": """
        SELECT c.customer_name, 
               ROUND(SUM(oi.quantity * p.price * (1 - oi.discount_percent / 100)), 2) AS total_revenue
        FROM customers c
        JOIN orders o ON o.customer_id = c.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY c.customer_id
        ORDER BY total_revenue DESC
        LIMIT 10;
    """,
    "query2_monthly_revenue": """
        SELECT 
    YEAR(o.order_date) AS year,
    MONTH(o.order_date) AS month_num,
    MIN(MONTHNAME(o.order_date)) AS month_name,
    ROUND(SUM(oi.quantity * p.price * (1 - oi.discount_percent / 100)), 2) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY YEAR(o.order_date), MONTH(o.order_date)
ORDER BY year, month_num;

    """,
    "query3_top_products": """
        SELECT p.product_name,
               SUM(oi.quantity) AS total_quantity,
               ROUND(SUM(oi.quantity * p.price), 2) AS total_sales
        FROM products p
        JOIN order_items oi ON p.product_id = oi.product_id
        GROUP BY p.product_id
        ORDER BY total_sales DESC
        LIMIT 5;
    """,
    "query4_region_sales": """
        SELECT r.region_name,
               ROUND(SUM(oi.quantity * p.price), 2) AS total_sales
        FROM regions r
        JOIN customers c ON r.region_id = c.region_id
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY r.region_name
        ORDER BY total_sales DESC;
    """,
    "query5_avg_order_value": """
        SELECT c.customer_name,
               ROUND(AVG(oi.quantity * p.price), 2) AS avg_order_value
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY c.customer_id
        ORDER BY avg_order_value DESC
        LIMIT 10;
    """,

    "query6_product_sales_revenue" : """
        SELECT 
        p.product_name,
        ROUND(SUM(oi.quantity * p.price * (1 - oi.discount_percent/100)), 2) AS total_revenue
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY p.product_id, p.product_name
    ORDER BY total_revenue DESC
    LIMIT 5;
    """,
    "query7_revenue_by_region" : """ 
        SELECT 
        r.region_name,
        ROUND(SUM(oi.quantity * p.price * (1 - oi.discount_percent/100)), 2) AS total_revenue
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    JOIN regions r ON c.region_id = r.region_id
    GROUP BY r.region_id, r.region_name
    ORDER BY total_revenue DESC;
"""
}

# ---------- RUN & PLOT ----------
def plot_and_save(df, x, y, title, kind="bar", rotation=45):
    ax = df.plot(x=x, y=y, kind=kind, legend=False, figsize=(8, 5))
    plt.title(title)
    plt.xticks(rotation=rotation)
    plt.ylabel(y)
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, f"{title.replace(' ', '_').lower()}.png")
    plt.savefig(filepath)
    plt.close()
    print(f"✅ Saved chart: {filepath}")

for name, sql in queries.items():
    df = pd.read_sql(sql, engine)
    print(f"\n▶ Running {name}...\n", df.head())

    if name == "query1_revenue_by_customer":
        plot_and_save(df, "customer_name", "total_revenue", "Top 10 Customers by Revenue")
    elif name == "query2_monthly_revenue":
        plot_and_save(df, "month_name", "total_revenue", "Monthly Revenue Trend", kind="line", rotation=30)
    elif name == "query3_top_products":
        plot_and_save(df, "product_name", "total_sales", "Top 5 Products by Sales")
    elif name == "query4_region_sales":
        plot_and_save(df, "region_name", "total_sales", "Sales by Region")
    elif name == "query5_avg_order_value":
        plot_and_save(df, "customer_name", "avg_order_value", "Top 10 Customers by Avg Order Value")
    elif name == "query6_product_sales_revenue":
        plot_and_save(df, "product_name", "total_revenue", "Top 5 Products by Sales Revenue")
    elif name == "query7_revenue_by_region":
        plot_and_save(df, "region_name", "total_revenue", "Revenue by Each Region")

print("\n🎉 All queries executed and charts saved in 'output/' folder!")
