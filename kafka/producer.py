# producer.py
from kafka import KafkaProducer
import pandas as pd
import json

# Leer datos limpios y enviar a Kafka
data = pd.read_csv("../dataset/cleaned_data.csv")

producer = KafkaProducer(bootstrap_servers="localhost:9092",
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for _, row in data.iterrows():
    message = row[["Economy (GDP per Capita)", "Family", "Health (Life Expectancy)", "Freedom",
                   "Trust (Government Corruption)", "Generosity", "Dystopia Residual"]].to_dict()
    producer.send("happiness_topic", message)

print("Mensajes enviados al tópico de Kafka.")
producer.flush()
