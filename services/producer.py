from kafka import KafkaProducer
from json import dumps, loads
import time
from services.datos import transform

print('--------------Kafka App--------------')

def kafka_producer():
    print("---------Enviando Mensajes----------")
    df = transform()
    producer = KafkaProducer(
        value_serializer = lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092'],
    )
    time.sleep(0.5)
    try:
        for index, row in df.iterrows():
            message = row.to_dict()
            print(message)
            print("Mensaje Enviado")
            producer.send("workshop3", value=message)
            time.sleep(0.01)
    except:
        print("No hay mas mensajes")
    


       
