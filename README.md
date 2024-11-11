<!DOCTYPE html>
<html>
<head>
  <style>
    h1 { color: #2c3e50; font-size: 2em; }
    h2 { color: #34495e; font-size: 1.5em; }
    p, li { font-size: 1.1em; color: #2d3436; }
    code { background-color: #ecf0f1; padding: 2px 4px; border-radius: 4px; }
  </style>
</head>
<body>

<h1>Workshop 3: Machine Learning and Data Streaming</h1>

<p><strong>Author:</strong> Ana Cristina Quintero</p>
<p><strong>Course:</strong> Data Engineering and IA - Universidad Autónoma de Occidente</p>
<p><strong>Date:</strong> November 13, 2024</p>

<h2>Introduction</h2>
<p>This project involves working with five CSV files containing information on happiness scores in different countries and years. The objective was to train a regression model to predict the happiness score. The following steps were taken:</p>
<ul>
  <li>Performed a complete EDA/ETL process to extract features from the files.</li>
  <li>Trained the regression model with a 70-30 data split for training and testing.</li>
  <li>Implemented a data streaming pipeline using Kafka to predict happiness scores and store the predictions in a database along with the respective features.</li>
  <li>Evaluated the model using performance metrics on the test set.</li>
</ul>

<h2>Exploratory Data Analysis (EDA)</h2>
<p>During the exploratory analysis, null values were identified and removed in several columns, allowing us to work only with valuable data. The main findings from the analysis are:</p>
<ul>
  <li>The most influential variables for happiness were <strong>Economy</strong>, <strong>Health</strong>, and <strong>Family Support</strong>.</li>
  <li>A correlation matrix was created to determine the variables with the strongest relationships.</li>
  <li>Distribution and analysis of key variables such as economy, family, health, freedom, and trust in government.</li>
</ul>

<h2>Models</h2>
<p>Four linear regression models were tested with the following results:</p>
<pre>
Model    MSE     R2
1         0.12    0.89
2         0.37    0.69
3         0.24    0.80
4         0.12    0.90
</pre>
<p><strong>Model 4</strong> was selected as the best due to its low error and high <code>R2</code> value, indicating that it captures the relationships in the data more effectively. This model was saved in a specific folder for use in the data streaming pipeline.</p>

<h2>Kafka Process</h2>
<p>To manage real-time data flow, an architecture was implemented using Kafka, organized in folders to handle the roles of <code>producer</code>, <code>consumer</code>, and <code>master</code>. The purpose of this structure is as follows:</p>
<ul>
  <li>Collect input data through the producer.</li>
  <li>Process and predict the happiness score in real-time through the consumer using the trained model.</li>
  <li>Store the predictions in a database.</li>
</ul>
<p>To facilitate deployment, Docker was used, where each component was defined as a container, allowing for scalable and efficient implementation of the Kafka infrastructure.</p>

<h2>System Validation</h2>
<ul>
  <li>The IP <code>localhost:6080</code> was used to validate the system's operation by configuring a new server and using the defined credentials.</li>
  <li>The database was checked to ensure that the corresponding table was empty before starting the process.</li>
  <li>Using <strong>pgAdmin</strong>, we verified that the data was correctly stored in the table after each execution of the data flow.</li>
</ul>

<h2>Conclusion</h2>
<p>This project demonstrates the integration of machine learning with real-time data streaming using Kafka and Docker. The implemented structure allows continuous data processing and happiness score prediction, storing results in a database for further analysis.</p>

</body>
</html>
