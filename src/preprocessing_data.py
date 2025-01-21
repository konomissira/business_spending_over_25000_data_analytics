import pandas as pd
from datetime import datetime
import os

# Load the dataset
def load_data(file_path):
    return pd.read_csv(file_path, encoding='ISO-8859-1')

# Drop columns with no data
def drop_empty_columns(data):
    empty_columns = ['Contract Number', 'Project Code', 'Expenditure Type']
    return data.drop(columns=empty_columns)

# Clean and normalize categorical data
def normalize_categorical_data(data, columns):
    for col in columns:
        data[col] = data[col].str.strip().str.lower()
    return data

# Handle missing values
def handle_missing_values(data):
    data['Supplier Post Code'].fillna('unknown', inplace=True)
    data['Supplier Type'].fillna('unknown', inplace=True)
    return data

# Convert date columns to datetime format
def convert_dates(data, date_column):
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce', dayfirst=True)
    return data

# Feature engineering: extract year and month from date
def extract_date_features(data, date_column):
    data['Year'] = data[date_column].dt.year
    data['Month'] = data[date_column].dt.month
    return data

# Save the cleaned data
def save_cleaned_data(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)

# Main preprocessing function
def preprocess_data(input_path, output_path):
    # Load data
    data = load_data(input_path)
    
    # Drop empty columns
    data = drop_empty_columns(data)
    
    # Clean and normalize data
    categorical_columns = ['Department', 'Entity', 'Expense Type', 'Expense Area', 'Supplier', 'Supplier Post Code', 'Supplier Type']
    data = normalize_categorical_data(data, categorical_columns)
    
    # Handle missing values
    data = handle_missing_values(data)
    
    # Convert dates and extract features
    data = convert_dates(data, 'Date of Payment')
    data = extract_date_features(data, 'Date of Payment')
    
    # Save the preprocessed data
    save_cleaned_data(data, output_path)
    print(f"Data preprocessing completed successfully! Processed data saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    input_file = "../data/raw_data/bis_spending_dpt_of_business.csv"
    output_file = "../data/processed_data/cleaned_data.csv"
    preprocess_data(input_file, output_file)
