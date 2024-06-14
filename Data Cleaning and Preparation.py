import pandas as pd
# Load the dataset
file_path = 'C:/Users/e5658860/OneDrive - FIS/Documents/Job info/Test/Synthetic_Software_Sales_Data.csv' # Update with your file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
data.head()

# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)

# Drop rows with missing values
data_cleaned = data.dropna()

# Check for duplicates
duplicate_records = data_cleaned.duplicated().sum()
print(duplicate_records)

# Remove duplicate records
data_cleaned = data_cleaned.drop_duplicates()

# Descriptive statistics
descriptive_stats = data_cleaned.describe()
print(descriptive_stats)

# Check data types
data_cleaned.dtypes

# Convert 'Date of Sale' to datetime format
data_cleaned['Date of Sale'] = pd.to_datetime(data_cleaned['Date of Sale'], format='%d-%m-%Y')

# Create a new calculated field for Total Revenue
data_cleaned['Total Revenue'] = data_cleaned['Sales Amount in US$'] * data_cleaned['Units Sold']


# Save the cleaned dataset
cleaned_file_path = 'C:/Users/e5658860/OneDrive - FIS/Documents/Job info/Test/Cleaned_Software_Sales_Data.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)