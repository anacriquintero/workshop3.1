# consumer.py
from kafka import KafkaConsumer
import joblib
import json
import sqlite3
import sys
sys.path.append("../connection_database")
from db_connection import create_connection

# Cargar el modelo
model = joblib.load("../connection_database/happiness_model.pkl")

# Conectar a la base de datos
conn = create_connection("happiness_predictions.db")

# Consumidor de Kafka
consumer = KafkaConsumer("happiness_topic", bootstrap_servers="localhost:9092",
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    features = message.value
    input_data = [[features["Economy (GDP per Capita)"], features["Family"], features["Health (Life Expectancy)"],
                   features["Freedom"], features["Trust (Government Corruption)"], features["Generosity"],
                   features["Dystopia Residual"]]]
    # Realizar predicción
    predicted_score = model.predict(input_data)[0]

    # Guardar en la base de datos
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO predictions (Economy, Family, Health, Freedom, Trust, Generosity, Dystopia, Predicted_Score)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (features["Economy (GDP per Capita)"], features["Family"], features["Health (Life Expectancy)"],
                    features["Freedom"], features["Trust (Government Corruption)"], features["Generosity"],
                    features["Dystopia Residual"], predicted_score))
    conn.commit()

    print(f"Predicción guardada: {predicted_score}")

conn.close()
