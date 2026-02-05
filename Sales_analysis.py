#import pandas for data manupulations
import pandas as pd 
#read the CSV file
df=pd.read_csv(r"C:\Users\Rittush\Downloads\sales_data.csv")
#print all tha data of CSV file
print(df) 
 #print top 10 data(rows)
print(df.head(10))
 #print last 10 data(column)
print(df.tail(10))
#print total rows columns,Dtype ,column name,memory usages
print(df.info()) 
#total no of row and column
print(df.shape) 
#Column name and dtype
print(df.columns) 
# perform operations such as count,mean,std,min,25%,50%,75% and max of numerical values
print(df.describe())
#check the missing values in dataset if the missing valye is found return True as an output otherwise return False
print(df.isnull())
#sum is count the missing value in particular column
print(df.isnull().sum())
#remove duplicates values
df = df.drop_duplicates()
#print duplicates value
print(df)
#calculate total sales
total_sales = df['Total_Sales'].sum()
#print total sales
print("Total Sales:", total_sales)
#revenue of particular product
df['Revenue'] = df['Quantity'] * df['Price']
#print the revenue
print(df["Revenue"])
#This code groups the data by product, sums the total sales for each product, sorts them in descending order, and returns the product with the highest total sales.
best_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(1)
#print the best product
print(best_product)