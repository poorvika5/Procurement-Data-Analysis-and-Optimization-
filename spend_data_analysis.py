
import pandas as pd
import matplotlib.pyplot as plt

# Load the aggregated data
supplier_aggregated_data = pd.read_csv('supplier_aggregated_data.csv')

# 1. Identify High-Spend Categories and Suppliers
high_spend_categories = supplier_aggregated_data.groupby('Category')['Total Spend'].sum().sort_values(ascending=False)
high_spend_suppliers = supplier_aggregated_data.groupby('Supplier Name')['Total Spend'].sum().sort_values(ascending=False)

# 2. Analyze Spend Over Time
procurement_data = pd.read_csv('procurement_data.csv')
procurement_data['Date'] = pd.to_datetime(procurement_data['Date'])
spend_over_time = procurement_data.groupby(procurement_data['Date'].dt.to_period("M"))['Total Spend'].sum()

# Plot High-Spend Categories
plt.figure(figsize=(10, 6))
high_spend_categories.plot(kind='bar', color='skyblue')
plt.title('Total Spend by Category')
plt.ylabel('Total Spend')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.savefig('total_spend_by_category.png')

# Plot High-Spend Suppliers
plt.figure(figsize=(10, 6))
high_spend_suppliers.head(10).plot(kind='bar', color='salmon')
plt.title('Top 10 High-Spend Suppliers')
plt.ylabel('Total Spend')
plt.xlabel('Supplier')
plt.xticks(rotation=45)
plt.savefig('top_spend_suppliers.png')

# Plot Spend Over Time
plt.figure(figsize=(10, 6))
spend_over_time.plot(kind='line', marker='o', color='green')
plt.title('Total Spend Over Time')
plt.ylabel('Total Spend')
plt.xlabel('Time (Monthly)')
plt.grid(True)
plt.savefig('spend_over_time.png')
