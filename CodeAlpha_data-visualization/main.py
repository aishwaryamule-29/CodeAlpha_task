from src.data_cleaning import load_data, clean_data, save_clean_data
from src.visualization import (
    monthly_sales_trend,
    sales_by_region,
    profit_distribution,
    sales_vs_profit
)

# Load data
df = load_data("data/raw/sales_data.csv")

# Clean data
clean_df = clean_data(df)

# Save cleaned data
save_clean_data(clean_df, "data/processed/cleaned_sales_data.csv")

# Generate visuals
monthly_sales_trend(clean_df)
sales_by_region(clean_df)
profit_distribution(clean_df)
sales_vs_profit(clean_df)

print("✅ Project executed successfully")