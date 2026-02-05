Sales Dataset Analysis Report
1. Introduction
This report presents a comprehensive analysis of a sales dataset using Python and the pandas library.
The analysis focuses on understanding the structure of the dataset, cleaning the data, calculating key statistics, computing revenue, and identifying the best-performing product.

2. Dataset Loading and Initial Inspection
The dataset was loaded using:
df = pd.read_csv(r"C:\Users\Rittush\Downloads\sales_data.csv")
Display Full Dataset
The complete dataset was printed to visually inspect its structure and values.
Top 10 Rows
df.head(10)
This gives a quick look at the first records.
Last 10 Rows
df.tail(10)
This helps verify the end of the dataset.

3. Dataset Structure
To understand data types, memory usage, and overall structure:
df.info()

Output Insight:
Displays column names
Shows data types (int, object)
Shows non-null values
Indicates memory usage
✔Shape of Dataset
df.shape
Gives total rows and total columns.
Column Names
df.columns

4. Summary Statistics
To understand numerical characteristics:
df.describe()

This produces metrics such as:
Count
Mean
Standard deviation
Minimum / Maximum
25%, 50%, 75% percentiles
These help identify trends and variations in quantity, price, and total sales.

5. Missing Value Analysis
df.isnull()
df.isnull().sum() #count no of missing value

Result:
No missing values were found in the dataset.
All columns contain complete data.

6. Duplicate Handling
Duplicate rows were removed using:
df = df.drop_duplicates()
This step ensures data quality and prevents skewed calculations.

7. Total Sales Calculation
total_sales = df['Total_Sales'].sum()

Insight:
The total sales value represents total revenue generated from all transactions.

8. Revenue Calculation
A new column Revenue was added to calculate item-wise revenue:
df['Revenue'] = df['Quantity'] * df['Price']

Purpose:
Helps validate Total_Sales values
Useful for product-wise revenue analysis

9. Best Product Identification
To find which product generated the highest total sales:
best_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(1)

Insight:
Groups data by each product
Calculates total sales per product
Sorts values from highest to lowest
Returns the top-performing product
