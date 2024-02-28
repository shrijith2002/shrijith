# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
data = pd.read_csv('Top Indian Places to Visit 2.csv')

print(data.columns)

# Displaying the first few rows of the dataset
print(data.head(5))

# Function to create a bar chart
def plot_bar_chart(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_column, y=y_column, data=data)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Bar Chart')
    plt.xticks(rotation=45)
    plt.show()

# Function to create a line graph
def plot_line_graph(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_column, y=y_column, data=data, marker='o')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Line Graph')
    plt.xticks(rotation=45)
    plt.show()

# Function to create a box plot
def plot_box_plot(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_column, y=y_column, data=data)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Box Plot')
    plt.xticks(rotation=45)
    plt.show()

# Plot bar chart
plot_bar_chart(data.head(15), 'Type', 'Google review rating')

# Plot line plot
plot_line_graph(data.head(30), 'Establishment Year', 'Google review rating')

# Example usage of the function
plot_box_plot(data, 'Zone', 'Google review rating')

# Descriptive statistics of the dataset
print(data.describe())

# Correlation matrix for numeric columns
numeric_data = data.select_dtypes(include='number')
correlation_matrix = numeric_data.corr()
print(correlation_matrix)
