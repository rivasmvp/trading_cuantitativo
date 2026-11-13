# Datos bursátiles en Python - Desarrollo de herramientas de trading cuantitativo.

> NO ES RECOMENDACION DE INVERSIÓN: Usá el engine bajo tu responsabilidad financiera, desalentamos su uso sin experiencia. Perder el 100% del capital es una posibilidad estadística en el mundo de las inversiones.


## Propósito general.
Notebooks interactivas de ánalisis de datos del mercado. Lo utilizo personalmente para mis inversiones y trading.

Elimina el sesgo emocional y ahorra horas de revisión manual de gráficos. En lugar de revisar 400 o 600 activos a mano, el script procesa la base de datos en segundos y devuelve únicamente los activos que cumplen con la estructura.

# Arquitectura del Sistema.

### 1.scraping.py -> 2.datos.py -> 3.fundamentales.py -> 4.sub módulo interactivo. 

1.scraping.py: Un script diseñado para la extracción ágil de tickers.

2.datos.py: Módulo de código con funciones centralizadas para conectarse a fuentes de datos bursátiles y descargar la información de los tickers.

3.fundamentales.py: Módulo para el seguimiento de flujos de datos fundamentales.

4.sub módulo interactivos con Jupyter Notebooks: Múltiples notebooks de escaneo técnico especializado
    -scanner_rsi.ipynb: Sobreventa universal en su indicador RSI. 
    -analisis_sectores.ipynb: Graficado por sectores. Precio y RSI.
    -scanner_emas.ipynb: Precio de cierre supera a media móvil EMA(n). 
    -scanner_macd.ipynb: Entradas en el MACD. 
    -scanner_pullback_ema200.ipynb: Activos que esten rebotando desde el soporte(EMA200)
    -indice_volatilidad.ipynb: Índice volatilidad VIX.

5. estrategia1/: Estructura de Estrategias y Trazabilidad: Contiene planes de trading operativos (estrategia1_plan.md), bitácoras de ejecución persistentes (journal.md) y módulos de validación y backtest (backtest_estrategia1/).




