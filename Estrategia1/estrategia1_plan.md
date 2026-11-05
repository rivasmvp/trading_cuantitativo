## 02/11/2026

## Resumen de la estrategia (+366.3%, Sharpe 1.17, DD 36.1%) backtest en QuantConnect resoludion diaria.

Universo: 277 CEDEARs operables (ETFs + megacaps USA verificadas con datos en QuantConnect). Resolución diaria.

Idea central: comprar activos en tendencia alcista firme, con timing de entrada por pullback, escalar la posición en dos tramos, y salir al año o cuando la tendencia se rompe.

Riesgo: DD 36%

## Cómo funciona el algoritmo
### 1. Ajuste

Capital: $2,5M

Máximo 8 posiciones simultáneas (slots)

Dos parámetros configurables: EMA de entrada (12).

Para cada activo hay 3 indicadores registrados: EMA200 (tendencia madre), EMA150 (tendencia secundaria), EMA12 (timing).

### 2. Señal de entrada.

Filtro macro: cierre > EMA150 y EMA200 subiendo en las últimas 20 ruedas (pendiente positiva). "Tendencia alcista sólida".

Trigger: cruce alcista del precio sobre la EMA12.

### 3. Cola y priorización

Si hay más señales que slots libres, las señales se meten a una cola. Cuando se libera un slot, entra la de mayor momentum de 3 meses, y una señal vencida de cola sólo entra si su condición sigue vigente (precio > EMA12 y EMA150 sana). Si ya no está en tendencia, sale de la cola sin comprarse.

### 4. Salidas

Venta incondicional a los 365 días (buy & hold de un año).

O anticipada si se pierde la tendencia: cierre < EMA150 y EMA150 cayendo en 20 ruedas.