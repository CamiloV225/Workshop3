from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import psycopg2

df = pd.read_csv("C:/Users/camil/Downloads/workshop3/resultado.csv")
print(df)

features = ['Happiness Rank','Happiness Score', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Health (Life Expectancy)', 'Generosity']

X = df[features]
y = df['Economy (GDP per Capita)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred_df = pd.DataFrame({'Economy (GDP per Capita)': y_pred})
y_pred_df['Economy (GDP per Capita)'] = y_pred_df['Economy (GDP per Capita)'].round(3)
print(y_pred_df)

df["Predicción Economy"] = y_pred_df
