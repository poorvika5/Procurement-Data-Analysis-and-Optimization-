
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the data
supplier_data = pd.read_csv('supplier_data.csv')
performance_data = pd.read_csv('performance_data.csv')

# Normalizing the performance metrics to a 0-1 scale using MinMaxScaler
scaler = MinMaxScaler()
performance_data[['On-time Delivery Rate (%)', 'Quality Score', 'Compliance Rate (%)', 'Contract Adherence (%)', 'Lead Time (Days)']] = scaler.fit_transform(
    performance_data[['On-time Delivery Rate (%)', 'Quality Score', 'Compliance Rate (%)', 'Contract Adherence (%)', 'Lead Time (Days)']])

# Inverse the lead time (lower is better, so higher normalized value should reflect better performance)
performance_data['Lead Time (Days)'] = 1 - performance_data['Lead Time (Days)']

# Calculate the overall performance score by averaging all the KPIs
performance_data['Performance Score'] = performance_data[
    ['On-time Delivery Rate (%)', 'Quality Score', 'Compliance Rate (%)', 'Contract Adherence (%)', 'Lead Time (Days)']].mean(axis=1)

# Rank Suppliers
performance_data['Rank'] = performance_data['Performance Score'].rank(ascending=False)

# Merge the performance data with supplier data for complete information
supplier_performance = pd.merge(supplier_data, performance_data, on='Supplier ID')
supplier_performance = supplier_performance.sort_values(by='Performance Score', ascending=False)

# Save the ranked supplier performance
supplier_performance.to_csv('supplier_performance_ranked.csv', index=False)
