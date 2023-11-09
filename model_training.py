import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("C:/Users/camil/Downloads/workshop3/resultado.csv")
X = df[['Economy (GDP per Capita)', 'Health (Life Expectancy)', 'Family']]
y = df['Happiness Score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12)
model = LinearRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print(f"Precisión del modelo: {accuracy}")
r2 = r2_score(y_test, y_pred)

#Prueba del modelo
example_features = [[0.306, 0.295, 0.575]] 
predicted_happiness = model.predict(example_features)

print(f"Estimación de felicidad: {predicted_happiness}")

joblib.dump(model, 'modelo_regresion.pkl')