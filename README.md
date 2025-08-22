# 📊 Sales Dashboard (SQL + Python)

A data-driven **Sales Analytics Dashboard** built with **MySQL, SQLAlchemy, and Pandas**.  
This project runs complex SQL queries, automates data extraction, and generates clear **CSV outputs and visual insights** — making sales reporting faster, smarter, and more interactive.

## What’s inside

- `dashboard_charts.py`: runs 4-5 SQL queries, saves CSVs to `output/`, generates charts (if enabled).
- `connect_mysql.py`: sample MySQL connection (SQLAlchemy).
- `sql/`: any reusable SQL snippets.
- `output/`: CSV results (and optional charts).
- `requirements.txt`: project dependencies.

## 📊 Queries Covered

This project explores the `sales_dashboard` database to answer real-world business questions, helping stakeholders understand **customers, products, revenue, and regions**.

1. **Top Customers by Revenue** – Highlights the top 5 customers driving the highest sales revenue.
2. **Monthly Revenue Trend** – Tracks revenue growth patterns over time (by year and month).
3. **Top Selling Products** – Identifies the most frequently purchased products.
4. **Category-wise Revenue Contribution** – Shows revenue share across different product categories.
5. **Region-wise Sales Performance** – Compares sales performance across regions to assess market strength.
6. **Top Products by Sales Revenue** – Calculates revenue per product, considering **quantity × price × discount**.
7. **Revenue by Region** – Analyzes total revenue per region by combining customer, product, and discount data.

## 📈 Visual Outputs

Along with SQL queries, this project generates **data visualizations** using Python (Pandas, Matplotlib).  
Each chart is saved as a PNG file in the `output/` folder.

- **Top Customers by Revenue** → Bar chart showing top 5 customers.
- **Monthly Revenue Trend** → Line chart displaying sales growth over months.
- **Top Selling Products** → Bar chart of most frequently purchased products.
- **Category-wise Revenue Contribution** → Pie chart of revenue share by category.
- **Region-wise Sales Performance** → Bar chart comparing revenue across regions.
- **Top 5 Products by Sales Revenue** → Bar chart ranking products by total sales revenue.
- **Revenue by Region** → Bar chart showing overall revenue across customer regions.

## How to run

1. Create `.venv` and install deps:
   ```bash
   pip install -r requirements.txt
   rements.txt
   ```

## 📂 Sample Outputs

Example CSV outputs are stored in the `output/` folder.  
Example chart images can be generated and saved (if enabled).

**Top Customers by Revenue (sample):**
| Customer Name | Total Revenue |
|---------------|---------------|
| Alice Corp | 12000.50 |
| Beta Ltd | 10500.00 |

_(Charts will appear in `/charts` if generated.)_
