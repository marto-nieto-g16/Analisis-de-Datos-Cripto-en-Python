import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

symbol = "BTC-USD"
data = yf.download(symbol, start="2020-12-01", end="2023-05-15")

# Extraer los precios de cierre y fechas en un DataFrame
df = pd.DataFrame({'Date': data.index, 'Close': data['Close']})

# Dividir los datos en entrenamiento y prueba
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

# Convertir las fechas a un formato numérico compatible
train_dates = (train_data['Date'].values.astype(np.int64) // 10**9).reshape(-1, 1)
test_dates = (test_data['Date'].values.astype(np.int64) // 10**9).reshape(-1, 1)

# Obtener los precios de cierre correspondientes
train_prices = train_data['Close'].values.reshape(-1, 1)
test_prices = test_data['Close'].values.reshape(-1, 1)

# Crear y entrenar el modelo de regresión lineal
reg = LinearRegression()
reg.fit(train_dates, train_prices)

# Realizar la predicción
predicted_prices = reg.predict(test_dates)

# Visualizar los resultados
plt.scatter(train_dates, train_prices, color='blue', label='Train Data')
plt.scatter(test_dates, test_prices, color='green', label='Test Data')
plt.plot(test_dates, predicted_prices, color='red', label='Prediction')
plt.legend()
plt.show()

# Imprimir el precio predicho más reciente
print("A predicted price of: $", int(predicted_prices[-1][0]))
