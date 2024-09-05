
from scipy.optimize import linprog
import pandas as pd
import numpy as np

# Load the top suppliers data (example for top 10 based on spend)
top_suppliers_data = pd.read_csv('supplier_aggregated_data.csv').head(10)
performance_data = pd.read_csv('performance_data.csv')

# Merge the supplier performance data with the top suppliers data
top_suppliers_performance = pd.merge(top_suppliers_data, performance_data[['Supplier ID', 'Performance Score']], on='Supplier ID', how='left')

# Define the objective coefficients (unit costs)
c = top_suppliers_performance['Unit Price'].values

# Define the bounds for each supplier's spend (0 to unlimited for simplicity)
x_bounds = [(0, None) for _ in range(len(c))]

# Solve the linear programming problem with no constraints, just minimizing costs
res_min_cost = linprog(c, bounds=x_bounds, method='highs')

# Display the results with no constraints
optimized_spends_min_cost = res_min_cost.x
total_cost_min_cost = res_min_cost.fun

# Adding optimized spends back to the dataframe
top_suppliers_performance['Optimized Spend (Min Cost)'] = optimized_spends_min_cost

# Save the optimized spends
top_suppliers_performance.to_csv('optimized_spends.csv', index=False)
