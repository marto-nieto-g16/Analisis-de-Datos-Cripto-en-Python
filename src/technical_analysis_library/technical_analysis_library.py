import yfinance as yf
import ta

# Símbolo de la criptomoneda que deseas analizar
symbol = "BTC-USD"

# Obtener datos históricos utilizando yfinance
data = yf.download(symbol, start="2022-01-01", end="2023-01-01")  # Ajusta las fechas según tus necesidades

# Calcular el Índice de Fuerza Relativa (RSI)
data["RSI"] = ta.momentum.RSIIndicator(data["Close"]).rsi()

# Calcular el Promedio Ponderado Móvil (MWA)
data["MWA"] = ta.trend.ema_indicator(data["Close"], window=20)

# Calcular la Divergencia de Convergencia del Promedio Móvil (MACD)
macd = ta.trend.macd_diff(data["Close"])
data["MACD"] = macd

# Determinar si es un año alcista o bajista
if data["RSI"].iloc[-1] > 70 and data["MWA"].iloc[-1] > data["MWA"].iloc[-2] and macd.iloc[-1] > 0:
    print("El patrón de precios sugiere un año alcista para Bitcoin (BTC).")
else:
    print("El patrón de precios sugiere un año bajista para Bitcoin (BTC).")
