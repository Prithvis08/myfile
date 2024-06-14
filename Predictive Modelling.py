import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Load and Prepare the Data
# Update with your file path
file_path = 'C:/Users/e5658860/OneDrive - FIS/Documents/Job info/Test/Cleaned_Software_Sales_Data.csv'
data_cleaned = pd.read_csv(file_path)

# Convert 'Date of Sale' to datetime format
data_cleaned['Date of Sale'] = pd.to_datetime(
    data_cleaned['Date of Sale'], format='ISO8601')

# Extract month and year for use in the model
data_cleaned['Month'] = data_cleaned['Date of Sale'].dt.month
data_cleaned['Year'] = data_cleaned['Date of Sale'].dt.year

# Step 2: Split the Data into Training and Testing Sets
X = data_cleaned[['Month', 'Marketing Spend in US$']]
y = data_cleaned['Sales Amount in US$']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Step 3: Build and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make Predictions and Evaluate the Model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Optional: Plotting the results for better visualization
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions)
plt.xlabel('Actual Sales Amount in US$')
plt.ylabel('Predicted Sales Amount in US$')
plt.title('Actual vs Predicted Sales Amount')
plt.grid(True)
plt.show()
