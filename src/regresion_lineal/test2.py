import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression

# Símbolo de la criptomoneda que deseas analizar
symbol = "BTC-USD"

# Obtener datos históricos utilizando yfinance
data = yf.download(symbol, start="2018-05-18", end="2023-05-18")  # Ajusta las fechas según tus necesidades

# Preparar los datos de entrenamiento
X = np.array(range(len(data))).reshape(-1, 1)
y = data["Close"].values

# Crear y ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predecir el precio para los últimos 5 años
next_years = range(data.index[-1].year + 1, data.index[-1].year + 6)
predicted_prices = model.predict(X[-5:])

for year, price in zip(next_years, predicted_prices):
    print(f"Año {year}: {int(price)}")
