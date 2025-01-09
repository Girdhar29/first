
# TASK 2 :

# Data Handling and Visualization :
#     1. Load a CSV file containing a dataset of your choice using Pandas. Perform the following:
#         - Display the first 5 rows and basic statistics.
#         - Handle any missing values by replacing them with the column mean.
#         - Create a new column based on a conditional logic (e.g., categorize a numeric column into "High", "Medium", and "Low").


import numpy as np
import pandas as pd

test = pd.read_csv('visa_stocks.csv')

print(test.head())
#checking null value
print(test.isnull().sum())

#There is no missing value for handle but if there is any missing value and we want to handel then we have to apply this code 
for col in test.columns:
    if pd.api.types.is_numeric_dtype(test[col]):
        test[col] = test[col].fillna(test[col].mean())

#And the Print the updated data to verify
print(test.isnull().sum())




# Define bins and labels for categorization
bins = [0, 50, 100, float('inf')]  # Example bins, adjust as needed
labels = ['Low', 'Medium', 'High']

# Create a new column 'open_category' based on the 'open' column values
test['open_category'] = pd.cut(test['Open'], bins=bins, labels=labels, right=False)

# Print the updated data to verify the categorization from the top 5
print(test.head())

# Print the updated data to verify the categorization from the lowest 5
print(test.tail())


############################################################################################################################################


#  3. Using Matplotlib and Seaborn:
#         - Plot a histogram of a numerical column from the dataset.
#         - Create a scatter plot for two numerical columns, including a regression line.


import matplotlib.pyplot as plt
import seaborn as sns


# ploting Histogram of 'Volume' column from the visa stock data set
plt.figure(figsize=(8, 6))
sns.histplot(test['Volume'], kde=True)  # Include kde for density estimation
plt.title('Distribution  Volume')
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.show()

# Ploting a scatter plot of 'Open' vs 'Close' with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='Open', y='Close', data=test)
plt.title('Open vs. Close Price')
plt.xlabel('Open Price')
plt.ylabel('Close Price')
plt.show()