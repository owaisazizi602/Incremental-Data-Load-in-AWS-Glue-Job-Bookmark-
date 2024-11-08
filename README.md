
![Screenshot 2024-11-09 at 00 15 14](https://github.com/user-attachments/assets/8202ef42-8764-4728-a815-aa740016d9b2)




This project demonstrates an incremental data load in AWS Glue using a Spark job. The project simulates loading telecom subscription data into an S3 bucket, with each file representing a daily update. By enabling and disabling AWS Glue's job bookmark feature, this project highlights the difference in handling incremental loads and avoiding duplicate records.

Architecture

Data Ingestion:
Three telecom subscription CSV files are stored in an S3 bucket in the telecom-catalog-project folder.

Data Cataloging with AWS Glue Crawler:
An AWS Glue Crawler is set up on the S3 bucket folder to catalog the files.
The metadata is stored in a database called telecom_catalog in the AWS Glue Data Catalog.

ETL with AWS Glue and Job Bookmark:
A Spark ETL job is created in AWS Glue without the job bookmark feature initially.
AWS CloudWatch is used to monitor record counts after each ETL job run to observe changes.

Incremental Load Testing:
When the job bookmark feature is disabled, each job run processes all files in the S3 bucket folder, leading to record duplication.
When the job bookmark feature is enabled, AWS Glue only processes new files, preventing duplication and achieving true incremental loading.

Process Flow

Upload Initial File:
The first file, customer_subscription_2023_08_21.csv, is uploaded to the S3 folder.
The crawler catalogs the folder, and the ETL job is run without the job bookmark, producing a total of 20 records.

Upload Additional Files (without Crawler Refresh):
The second file, customer_subscription_2023_08_22.csv, is added to the folder without re-running the crawler.
Running the ETL job without the job bookmark results in a total of 30 records, duplicating the initial 20 records due to the entire folder being processed again.

Enabling Job Bookmark:
The Spark script is updated to enable the job bookmark feature.
With only one file in the folder, the ETL job processes and produces 20 records.
Upon adding the second file, the job bookmark ensures only the new file’s 10 records are processed without reprocessing the previous 20 records, yielding a correct total of 10 records for the new data.

Monitor in CloudWatch:
Record counts are observed in AWS CloudWatch logs to validate the incremental loading behavior.

Key Components
Amazon S3: Storage for telecom subscription data files.
AWS Glue Crawler: Scans and catalogs the S3 data folder, storing metadata in AWS Glue Data Catalog.
AWS Glue Data Catalog: Stores metadata and table definitions for easy access.
AWS Glue Spark ETL Job:
Runs with and without the job bookmark feature to demonstrate its effect on incremental loading.
AWS CloudWatch: Monitors record counts and ETL job performance.
