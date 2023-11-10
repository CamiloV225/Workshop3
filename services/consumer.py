import pandas as pd
import joblib
from services.db import upload_data
from sklearn.metrics import mean_squared_error
from kafka import  KafkaConsumer
from json import dumps, loads
import time

print('--------------Kafka Consumer--------------')

def kafka_consumer():
    df = pd.read_csv('/home/camilo/docker/workshop3/data/resultados.csv')
    filas = len(df)
    print(filas)
    loaded_model = joblib.load('/home/camilo/docker/workshop3/model/modelo_regresion.pkl')
    consumer = KafkaConsumer(
        'workshop3',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )
    list_of_dfs = []
    mensajes_consumidos = 0
    print("---------Esperando Mensajes----------")
    for message in consumer:
        time.sleep(1)
        try:
            json_data = message.value
            print(json_data)
            df = pd.DataFrame.from_dict([json_data])
            #loaded_model = joblib.load('/home/camilo/docker/workshop3/model/modelo_regresion.pkl')
            example_features = df[['Economy (GDP per Capita)', 'Health (Life Expectancy)', 'Family','Freedom']].values
            predicted_happiness = loaded_model.predict(example_features.reshape(1, -1))
            #mse = mean_squared_error(example_features, predicted_happiness)
            #print(f"Mean Squared Error: {mse}")
            df['Predicted Happiness'] = predicted_happiness
            print(f"Estimated happiness: {predicted_happiness}")
            print(df)
            list_of_dfs.append(df)
            mensajes_consumidos += 1
            upload_data(df)

            
        except Exception as e:
            print(f"Error processing message: {e}")
            consumer.close()
            break

        final_df = pd.concat(list_of_dfs, ignore_index=True)
        final_df.to_csv('combined_dataframe.csv', index=False)
        if mensajes_consumidos >= filas: #
            print("No hay más mensajes.")
            break
    consumer.close()


       
