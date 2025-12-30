# step 1 import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# step 2 load the sales data
file_path = r"C:\Users\ABHILIPSA PATI\OneDrive\Desktop\PYTHON DA\vgsales.csv"
df = pd.read_csv(file_path)

# step 3 display the original data 
print(df.head())
print(df.info())
print(df.describe())

# step 4 check for missing values
print("\n=== checking Missing Values ===\n")
print(df.isnull().sum())

# Step 5: Handling missing values

# Fill missing values in 'Year' with median
df['Year'].fillna(df['Year'].median(), inplace=True)

# Fill missing values in 'Publisher' with 'Unknown'
df['Publisher'].fillna('Unknown', inplace=True)

# Verify missing values are handled
print(df.isnull().sum())
print("\n===  rechecking Missing Values ===\n")

# Step 6: remove duplicates
df.drop_duplicates(inplace=True) #drop rows with duplicate values
print("\n=== after removing duplicates ===\n")
print(df.head())
print(df.info())
print(df.describe())
 
# Step 7: Total sales per product

# Group by product name and calculate total global sales
product_sales = df.groupby('Name')['Global_Sales'].sum().reset_index()

# Sort products by total sales (descending order)
product_sales = product_sales.sort_values(by='Global_Sales', ascending=False)
print("\n=== Total Sales per Product ===\n")
print(product_sales)
# Display top 5 selling products
top_5_products = product_sales.head(5)

print("\n=== Top 5 Best-Selling Products ===\n")
print(top_5_products)

# Step 8: total sales per region and yearly trends
# total sales per region
region_sales = df.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().reset_index()
print("\n=== Total Sales per Region by Year ===\n") 
print(region_sales)

#total sales per yearly trends
yearly_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()
print("\n=== Yearly Global Sales ===\n")
print(yearly_sales)

# total sales per genre
genre_sales = df.groupby('Genre')['Global_Sales'].sum().reset_index()
genre_sales = genre_sales.sort_values(by='Global_Sales', ascending=False)
print("\n=== Total Sales per Genre ===\n")
print(genre_sales)
# total sales per publisher
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().reset_index()
publisher_sales = publisher_sales.sort_values(by='Global_Sales', ascending=False)
print("\n=== Total Sales per Publisher ===\n")
print(publisher_sales)
# total sales per platform
platform_sales = df.groupby('Platform')['Global_Sales'].sum().reset_index()
platform_sales = platform_sales.sort_values(by='Global_Sales', ascending=False)
print("\n=== Total Sales per Platform ===\n")
print(platform_sales)

# Step 9: Data Visualization (Top 10 Best-Selling Games)

# Select top 10 products
top_10 = product_sales.head(10)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10,
    x='Name',
    y='Global_Sales',
    palette='viridis'
)

plt.title('Top 10 Best-Selling Games')
plt.xlabel('Game Name')
plt.ylabel('Global Sales (Millions)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show(block=True)

# Step 10: Total Sales per Region

region_totals = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

plt.figure(figsize=(8, 5))
sns.barplot(x=region_totals.index, y=region_totals.values, palette='coolwarm')

plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (Millions)')
plt.tight_layout()
plt.show(block=True)

# Step 11: Total Sales per Year

plt.figure(figsize=(10, 5))
sns.lineplot(data=yearly_sales, x='Year', y='Global_Sales', marker='o')

plt.title('Global Sales Trend Over Years')
plt.xlabel('Year')
plt.ylabel('Total Global Sales (Millions)')
plt.grid(True)
plt.tight_layout()
plt.show(block=True)

# Step 12: Total Sales per Genre

plt.figure(figsize=(10, 6))
sns.barplot(
    data=genre_sales,
    x='Genre',
    y='Global_Sales',
    palette='Set2'
)

plt.title('Total Sales by Genre')
plt.xlabel('Genre')
plt.ylabel('Global Sales (Millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)

# Step 13: Total Sales per Publisher (Top 10)

top_publishers = publisher_sales.head(10)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_publishers,
    x='Publisher',
    y='Global_Sales',
    palette='rocket'
)

plt.title('Top 10 Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Global Sales (Millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)

# Step 14: Total Sales per Platform

plt.figure(figsize=(10, 6))
sns.barplot(
    data=platform_sales,
    x='Platform',
    y='Global_Sales',
    palette='mako'
)

plt.title('Total Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Global Sales (Millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)
