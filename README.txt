
# Procurement Data Analysis and Optimization Project

## Overview
This project focuses on developing a data-driven procurement optimization model to analyze spend data and supplier performance. The goal is to achieve cost reductions through bulk purchase discounts and renegotiating supplier contracts.

## Files Included

### 1. Python Scripts
- **data_extraction_and_preparation.py**: Script to load, clean, and prepare the data.
- **spend_data_analysis.py**: Script to analyze and visualize spend data.
- **supplier_performance_evaluation.py**: Script to evaluate and rank supplier performance.
- **procurement_optimization_model.py**: Script to run the procurement optimization model.

### 2. Data Files
- **supplier_data.csv**: Synthetic dataset containing supplier information.
- **procurement_data.csv**: Synthetic dataset containing procurement transaction details.
- **performance_data.csv**: Synthetic dataset containing supplier performance metrics.
- **supplier_aggregated_data.csv**: Aggregated data of supplier information with spend and unit price details.
- **top_suppliers_performance.csv**: Ranked supplier performance data.
- **optimized_spends.csv**: Output of the optimization model showing recommended spend allocations.

## How to Execute the Project

### Step 1: Set Up Your Environment
Ensure that Python is installed on your system. The following Python packages are required:
- pandas
- scipy
- matplotlib
- sklearn

You can install the required packages using pip:
```
pip install pandas scipy matplotlib scikit-learn
```

### Step 2: Run the Scripts

1. **Data Extraction and Preparation**
   - Execute the `data_extraction_and_preparation.py` script to load the data, clean it, and prepare it for analysis.
   - This will generate the `supplier_aggregated_data.csv` file.

   ```
   python data_extraction_and_preparation.py
   ```

2. **Spend Data Analysis**
   - Run the `spend_data_analysis.py` script to analyze the spend data and generate visualizations.
   - This script will generate PNG files such as `total_spend_by_category.png`, `top_spend_suppliers.png`, and `spend_over_time.png`.

   ```
   python spend_data_analysis.py
   ```

3. **Supplier Performance Evaluation**
   - Execute the `supplier_performance_evaluation.py` script to calculate and rank supplier performance based on various KPIs.
   - The output will be saved as `supplier_performance_ranked.csv`.

   ```
   python supplier_performance_evaluation.py
   ```

4. **Procurement Optimization Model**
   - Run the `procurement_optimization_model.py` script to perform procurement cost optimization.
   - The results will be saved as `optimized_spends.csv`.

   ```
   python procurement_optimization_model.py
   ```

### Step 3: Review the Results
After executing the scripts, review the generated CSV files and visualizations to understand the insights and recommendations provided by the analysis and optimization.

## Contact
If you have any questions or need further assistance, feel free to reach out.
