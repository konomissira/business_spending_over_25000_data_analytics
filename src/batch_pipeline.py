import pandas as pd
import os

# Load preprocessed data
def load_preprocessed_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

# Perform data transformations
def transform_data(data):
    # Aggregating total amount by year and month
    transformed_data = data.groupby(['Year', 'Month']).agg(
        total_amount=('Amount', 'sum'),
        transaction_count=('Transaction Number', 'count')
    ).reset_index()
    return transformed_data

# Save transformed data
def save_transformed_data(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Transformed data saved to: {output_path}")

# Main function to execute the batch pipeline
def batch_pipeline(input_path, output_path):
    try:
        # Step 1: Load preprocessed data
        data = load_preprocessed_data(input_path)
        
        # Step 2: Transform data
        transformed_data = transform_data(data)
        
        # Step 3: Save transformed data
        save_transformed_data(transformed_data, output_path)
        print("Batch pipeline executed successfully!")
    except Exception as e:
        print(f"Error during batch pipeline execution: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "../data/processed_data/cleaned_data.csv"
    output_file = "../data/transformed_data/aggregated_data.csv"
    batch_pipeline(input_file, output_file)