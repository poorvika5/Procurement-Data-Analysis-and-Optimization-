
import pandas as pd

# Load the data
supplier_data = pd.read_csv('supplier_data.csv')
procurement_data = pd.read_csv('procurement_data.csv')
performance_data = pd.read_csv('performance_data.csv')

# Convert 'Date' in procurement_data to datetime format
procurement_data['Date'] = pd.to_datetime(procurement_data['Date'])

# Check for missing values
print("Missing values in Supplier Data:\n", supplier_data.isnull().sum())
print("Missing values in Procurement Data:\n", procurement_data.isnull().sum())
print("Missing values in Performance Data:\n", performance_data.isnull().sum())

# Data Aggregation
# Aggregate total spend by supplier and category
total_spend_by_supplier = procurement_data.groupby(['Supplier ID', 'Category'])['Total Spend'].sum().reset_index()

# Calculate average unit price by supplier and category
avg_unit_price_by_supplier = procurement_data.groupby(['Supplier ID', 'Category'])['Unit Price'].mean().reset_index()

# Merge aggregated data back with supplier data for comprehensive analysis
supplier_aggregated_data = pd.merge(supplier_data, total_spend_by_supplier, on='Supplier ID')
supplier_aggregated_data = pd.merge(supplier_aggregated_data, avg_unit_price_by_supplier, on=['Supplier ID', 'Category'])

# Display the cleaned and aggregated data
supplier_aggregated_data.to_csv('supplier_aggregated_data.csv', index=False)
