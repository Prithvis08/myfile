import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = 'C:/Users/e5658860/OneDrive - FIS/Documents/Job info/Test/Cleaned_Software_Sales_Data.csv' # Update with your file path
data_cleaned = pd.read_csv(file_path)

# Generate descriptive statistics
descriptive_stats = data_cleaned.describe()
print(descriptive_stats)

# Grouping by date to analyze sales trends
data_cleaned['Date of Sale'] = pd.to_datetime(data_cleaned['Date of Sale'], format='ISO8601')
sales_trends = data_cleaned.groupby('Date of Sale')['Sales Amount in US$'].sum()

# Plotting sales trends over time
plt.figure(figsize=(10, 6))
plt.plot(sales_trends.index, sales_trends.values)
plt.title('Sales Trends Over Time')
plt.xlabel('Date of Sale')
plt.ylabel('Sales Amount in US$')
plt.grid(True)
plt.show()

# Grouping by region to analyze performance
region_performance = data_cleaned.groupby('Region')['Sales Amount in US$'].sum()

# Plotting region performance
plt.figure(figsize=(10, 6))
region_performance.plot(kind='bar', title='Region Performance', ylabel='Sales Amount in US$')
plt.show()

# Grouping by product type to analyze performance
product_performance = data_cleaned.groupby('Product Type')['Sales Amount in US$'].sum()

# Plotting product performance
plt.figure(figsize=(10, 6))
product_performance.plot(kind='bar', title='Product Performance', ylabel='Sales Amount in US$')
plt.show()


# Grouping by customer type to analyze purchase patterns
customer_patterns = data_cleaned.groupby('Customer Type')['Sales Amount in US$'].sum()

# Plotting customer patterns
plt.figure(figsize=(10, 6))
customer_patterns.plot(kind='bar', title='Customer Purchase Patterns', ylabel='Sales Amount in US$')
plt.show()

# Extracting the year of first purchase
data_cleaned['Year of First Purchase'] = data_cleaned['Date of Sale'].dt.year


# Cohort analysis to understand customer retention
cohort_analysis = data_cleaned.groupby(['Year of First Purchase', 'Returning Customer']).size().unstack()

# Plotting cohort analysis
plt.figure(figsize=(10, 6))
cohort_analysis.plot(kind='bar', stacked=True, title='Cohort Analysis of Customer Retention')
plt.show()