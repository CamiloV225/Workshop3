import mysql.connector
import json

def connect_mysql():
    with open('/home/camilo/docker/workshop3/services/db_config.json') as f:
        dbfile = json.load(f)
    
    connection = mysql.connector.connect(
        host=dbfile["host"],
        user=dbfile["user"],
        password=dbfile["password"],
        database=dbfile["database"]
    )
    
    #print("-----------Database Connected--------")
    return connection


def create_table():
    conn = connect_mysql()
    cursor = conn.cursor()
    H_predict = f"""CREATE TABLE IF NOT EXISTS happiness_prediction (
        id INT PRIMARY KEY AUTO_INCREMENT,
        Happiness_Score FLOAT,
        Economy FLOAT,
        Family FLOAT,
        Health FLOAT,
        Freedom FLOAT,
        Predicted FLOAT
        )
        """
    cursor.execute(H_predict)
    conn.commit()
    conn.close()
    print("------------Tabla Creada-----------")


def upload_data(df):
    print("------------Insertando Datos-----------")
    conn = connect_mysql()
    cursor = conn.cursor()
    create_table()

    row = df.iloc[0]
    query = f"""INSERT INTO happiness_prediction (Happiness_Score,Economy,Family,Health,Freedom,Predicted) 
            VALUES (%s,%s,%s,%s,%s,%s )"""
    cursor.execute(query, (row["Happiness Score"],row["Economy (GDP per Capita)"],row["Family"],row["Health (Life Expectancy)"],row["Freedom"],row["Predicted Happiness"]))
    conn.commit()
    conn.close()