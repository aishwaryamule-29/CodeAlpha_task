import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def monthly_sales_trend(df):
    monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
    monthly_sales.plot(kind='line', figsize=(8,5))
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig("outputs/figures/monthly_sales_trend.png")
    plt.show()

def sales_by_region(df):
    region_sales = df.groupby('Region')['Sales'].sum()
    plt.figure(figsize=(7,5))
    sns.barplot(x=region_sales.index, y=region_sales.values)
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("outputs/figures/sales_by_region.png")
    plt.show()

def profit_distribution(df):
    plt.figure(figsize=(7,5))
    sns.histplot(df['Profit'], bins=20, kde=True)
    plt.title("Profit Distribution")
    plt.xlabel("Profit")
    plt.tight_layout()
    plt.savefig("outputs/figures/profit_distribution.png")
    plt.show()

def sales_vs_profit(df):
    plt.figure(figsize=(7,5))
    sns.scatterplot(x='Sales', y='Profit', data=df)
    plt.title("Sales vs Profit")
    plt.tight_layout()
    plt.savefig("outputs/figures/sales_vs_profit.png")
    plt.show()