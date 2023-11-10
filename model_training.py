import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib

h_df = pd.read_csv("data/resultados.csv")


X = h_df[['Economy (GDP per Capita)', 'Health (Life Expectancy)', 'Family','Freedom']]
y = h_df['Happiness Score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12)
model = LinearRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)

#------------Metricas
mse = mean_squared_error(y_test, y_predict)
mean_ae = mean_absolute_error(y_test, y_predict)
accuracy = model.score(X_test, y_test) #### Es el mismo r^2
print(f"Precisión del modelo: {accuracy}")
print(f"Error medio absoluto: {mean_ae}")
print(f"Error cuadrático medio: {mse}")


#---------Prueba del modelo------------
example_features = [[0.306, 0.295, 0.575, 0.245]] 
predicted_happiness = model.predict(example_features)

print(f"Estimación de felicidad: {predicted_happiness}")

joblib.dump(model, '/home/camilo/docker/workshop3/model/modelo_regresion.pkl')