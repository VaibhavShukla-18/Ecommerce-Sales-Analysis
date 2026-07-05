import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# E-Commerce Sales Analysis
# ==============================

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# ==============================
# Basic Analysis
# ==============================

total_sales = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Total_Sales"].mean()

print("\n========== BUSINESS SUMMARY ==========")
print(f"Total Revenue       : ₹{total_sales:,.2f}")
print(f"Total Quantity Sold : {total_quantity}")
print(f"Average Sale Value  : ₹{average_sales:,.2f}")

# Top Selling Product
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

print("\nTop Selling Products")
print(product_sales)

# Region-wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)

print("\nSales by Region")
print(region_sales)

# Monthly Sales
df["Month"] = df["Date"].dt.strftime("%B")

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print("\nMonthly Sales")
print(monthly_sales)

# ==============================
# Data Visualization
# ==============================

# -------- Bar Chart --------
plt.figure(figsize=(8,5))
product_sales.plot(kind='bar', color='skyblue')

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/product_sales.png")
plt.close()


# -------- Line Chart --------
month_order = ["January", "February", "March", "April"]
monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(8,5))
monthly_sales.plot(kind='line', marker='o', linewidth=2)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)

plt.tight_layout()
plt.savefig("visualizations/monthly_sales.png")
plt.close()


# -------- Pie Chart --------
plt.figure(figsize=(7,7))

region_sales.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Sales Distribution by Region")
plt.ylabel("")

plt.tight_layout()
plt.savefig("visualizations/region_sales.png")
plt.close()

print("\n========================================")
print("All charts have been generated successfully!")
print("Saved in the 'visualizations' folder.")
print("========================================")