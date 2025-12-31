import pandas as pd

def load_data(file_path):
    """Load sales dataset"""
    return pd.read_csv("data/raw/sales_data.csv")

def clean_data(df):
    """Clean and preprocess data"""
    df = df.copy()

    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Handle missing values
    df.fillna({
        'Sales': df['Sales'].median(),
        'Profit': df['Profit'].median()
    }, inplace=True)

    return df

def save_clean_data(df, output_path):
    """Save cleaned data"""
    df.to_csv(output_path, index=False)