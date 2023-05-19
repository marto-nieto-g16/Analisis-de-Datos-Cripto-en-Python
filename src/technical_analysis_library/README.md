# Análisis de Patrón de Precios de Bitcoin (BTC)

Este código de Python utiliza la biblioteca `yfinance` y `ta` para realizar un análisis de patrón de precios de Bitcoin (BTC) utilizando indicadores técnicos comunes. Proporciona una estimación si el patrón de precios sugiere un año alcista o bajista para Bitcoin.

## Configuración
Antes de ejecutar el código, asegúrate de tener instaladas las bibliotecas `yfinance` y `ta`. Puedes instalarlas utilizando el siguiente comando:

```shell
pip install yfinance ta
```

## Uso
1. Define el símbolo de la criptomoneda que deseas analizar. Por ejemplo, si deseas analizar Bitcoin, puedes establecer `symbol = "BTC-USD"`. Asegúrate de utilizar el símbolo correcto para la criptomoneda que deseas analizar.

2. Ajusta las fechas de inicio y fin según tus necesidades. Por defecto, se establecen como `"2022-01-01"` y `"2023-01-01"` respectivamente. Estas fechas determinarán el rango de datos históricos utilizados para el análisis.

3. Ejecuta el código. Proporcionará una estimación si el patrón de precios sugiere un año alcista o bajista para Bitcoin.

## Indicadores Utilizados
El código utiliza los siguientes indicadores técnicos para el análisis:

- Índice de Fuerza Relativa (RSI): Calcula el índice de fuerza relativa basado en los precios de cierre.

- Promedio Ponderado Móvil (MWA): Calcula el promedio ponderado móvil basado en los precios de cierre.

- Divergencia de Convergencia del Promedio Móvil (MACD): Calcula la divergencia de convergencia del promedio móvil basada en los precios de cierre.

## Resultado
El código determina si el patrón de precios sugiere un año alcista o bajista para Bitcoin (BTC) utilizando los indicadores mencionados anteriormente. Imprime el resultado en la consola.

**Nota:** Ten en cuenta que el análisis de patrones de precios es una estimación y no garantiza resultados precisos. Es importante realizar un análisis adicional y considerar otros factores antes de tomar decisiones de inversión.

*Este código es proporcionado con fines educativos y no debe considerarse asesoramiento financiero.*