from confluent_kafka import Producer
import pandas as pd
import json
import time
def producer():
# Define the Confluent Kafka configurations
    conf = {
    'bootstrap.servers': 'localhost:9092',  # Sin prefijo de protocolo
    'security.protocol': 'PLAINTEXT',       # Usar PLAINTEXT
    # Otras configuraciones necesarias
}


# Initialize the producer with the configuration
    producer = Producer(conf)

# Load and iterate through the data
    data = pd.read_csv("../dataset/cleaned_data.csv")

    def delivery_report(err, msg):
        """Delivery report callback called once message is delivered or fails."""
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    for _, row in data.iterrows():
    # Convert the row data to JSON
        message = row[['Country','Happiness Rank','Happiness Score','Economy (GDP per Capita)',
                   'Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)',
                   'Generosity','Dystopia Residual','Year']].to_dict()

    # Produce the message to the topic with delivery report
        producer.produce("score", key=str(row['Country']), value=json.dumps(message), callback=delivery_report)
        print("mensaje enviado al topic score")
        time.sleep(1)
# Wait for any outstanding messages to be delivered
    producer.flush()
    print("Los mensajes han sido enviados con éxito al tópico de Confluent Kafka.")


if __name__=="__main__":
    producer()