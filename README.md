# Workshop 3: Machine Learning and Data Streaming

**Author:** Ana Cristina Quintero  
**Course:** Data Engineering and IA - Universidad Autónoma de Occidente  
**Date:** November 13, 2024  

## Introduction

This project involves working with five CSV files containing information on happiness scores in different countries and years. The objective was to train a regression model to predict the happiness score. The following steps were taken:
- Performed a complete EDA/ETL process to extract features from the files.
- Trained the regression model with a 70-30 data split for training and testing.
- Implemented a data streaming pipeline using Kafka to predict happiness scores and store the predictions in a database along with the respective features.
- Evaluated the model using performance metrics on the test set.

## Exploratory Data Analysis (EDA)

During the exploratory analysis, null values were identified and removed in several columns, allowing us to work only with valuable data. The main findings from the analysis are:
- The most influential variables for happiness were **Economy**, **Health**, and **Family Support**.
- A correlation matrix was created to determine the variables with the strongest relationships.
- Distribution and analysis of key variables such as economy, family, health, freedom, and trust in government.

## Models

Four linear regression models were tested with the following results:

| Model | MSE  | R²   |
|-------|------|------|
| 1     | 0.12 | 0.89 |
| 2     | 0.37 | 0.69 |
| 3     | 0.24 | 0.80 |
| 4     | 0.12 | 0.90 |

**Model 4** was selected as the best due to its low error and high R² value, indicating that it captures the relationships in the data more effectively. This model was saved in a specific folder for use in the data streaming pipeline.

## Kafka Process

To manage real-time data flow, an architecture was implemented using Kafka, organized in folders to handle the roles of **producer**, **consumer**, and **master**. The purpose of this structure is as follows:
- Collect input data through the producer.
- Process and predict the happiness score in real-time through the consumer using the trained model.
- Store the predictions in a database.

To facilitate deployment, Docker was used, where each component was defined as a container, allowing for scalable and efficient implementation of the Kafka infrastructure.

## System Validation

- The IP `localhost:6080` was used to validate the system's operation by configuring a new server and using the defined credentials.
- The database was checked to ensure that the corresponding table was empty before starting the process.
- Using **pgAdmin**, we verified that the data was correctly stored in the table after each execution of the data flow.

## Conclusion

This project demonstrates the integration of machine learning with real-time data streaming using Kafka and Docker. The implemented structure allows continuous data processing and happiness score prediction, storing results in a database for further analysis.
