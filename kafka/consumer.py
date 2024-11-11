from confluent_kafka import Consumer, KafkaError
import datetime
import joblib
import json
import pandas as pd
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append("../connection_database")
from db_connection import connection as db_connection
import time
def consumer ():

# Load the model
    model = joblib.load("../Models/happiness_model.pkl")

# Connect to the database
    conn = db_connection()

    conf = {
    'bootstrap.servers': 'localhost:9092',      # Dirección de tu broker de Kafka
    'group.id': 'happiness_score_consumer_group',  # Grupo de consumidores
    'auto.offset.reset': 'latest',            # Comenzar desde el inicio si no hay offset
    'security.protocol': 'PLAINTEXT'            # Protocolo de seguridad
    # No se requieren configuraciones de SASL/SSL para PLAINTEXT
}

# Initialize the Consumer
    consumer = Consumer(conf)
    consumer.subscribe(['score'])

# Initialize an empty DataFrame for storing results
    results = pd.DataFrame(columns=[
    "Economy (GDP per Capita)", "Family", "Health (Life Expectancy)", "Freedom",
          "Trust (Government Corruption)", "Generosity", "Dystopia Residual"
])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # Poll messages with a timeout of 1 second
            df = results.copy()
            if msg is None:
                continue  # Skip if no message is received
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue  # End of partition event
                else:
                    print(f"Error: {msg.error()}")
                    break  # Exit loop for critical errors

        # Parse message value as JSON
            kafka_value = json.loads(msg.value().decode('utf-8'))

        # Convert message to DataFrame
            new_data = pd.DataFrame([kafka_value], columns=[
            "Economy (GDP per Capita)", "Family", "Health (Life Expectancy)", "Freedom",
          "Trust (Government Corruption)", "Generosity", "Dystopia Residual"
        ])

        # Predict using the loaded model
            predicted_score = model.predict(new_data)[0]
            kafka_value['Predicted_Score'] = predicted_score

        # Append the prediction to the results DataFrame
            df = pd.concat([df, pd.DataFrame([kafka_value])], ignore_index=True)
            df.to_sql("score", con=conn, if_exists="append", index=False)
            print(f"[{datetime.datetime.now()}] - Data loaded into 'score' table")
        # Optional: Log each message and its prediction
            print(f"Processed message with prediction: {kafka_value}")
            
    except KeyboardInterrupt:
        print("Consumer interrupted manually")

    finally:
    # Save the DataFrame to PostgreSQL
        

    # Close connections
        consumer.close()
        conn.dispose()

if __name__=="__main__":
    consumer()