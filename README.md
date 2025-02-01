# business_spending_over_25000_data_analytics

## Project Overview

This project analyses spending data in the Department for Business, Innovation, and Skills (BIS) where expenditures exceed £25,000. The goal is to process and transform this data to generate insights, optimize spending patterns, and support data-driven decision-making.

## Features

-   **Data Ingestion**: Load and preprocess large CSV file.
-   **Data Transformation**: Perform aggregations, normalizations, and feature engineering.
-   **Batch and Scheduled Processing**:
    -   Initially implemented with cron jobs.
    -   Plan to transitioning to Apache Airflow for advanced scheduling and monitoring.
-   **Data Output**: Save transformed data in structured formats (CSV).

## Technologies Used

-   **Python**: Core programming language for ETL (Extract, Transform, Load) tasks.
-   **Apache Airflow** (planned): Orchestrates and schedules data pipelines.
-   **Pandas**: Data manipulation and transformation.
-   **MacOS**: Development environment.
-   **Git**: Version control.

## Installation and Setup

1. Clone the repository:
   
   git clone https://github.com/konomissira/business_spending_over_25000_data_analytics.git

   cd business_spending_over_25000_data_analytics

2. Set up a Python virtual environment: for **MacOS** User:
   
   python3 -m venv .venv -> (To create virtual environment)
   
   source .venv/bin/activate -> (To activate virtual environment)

4. Install required dependencies:
   
   pip install -r requirements.txt

## Run the Batch Pipeline

1. Navigate to the project directory:
   
   cd src
   python batch_pipeline.py
   
   View output file in the data/transformed_data/ directory.

## Future Enhancements

-   Integrate Apache Airflow: Replace cron jobs for better scheduling and monitoring.

-   Load data transformed data into S3 bucket

-   Data Visualization: Use Grafana or similar tools to visualize insights from transformed data.
