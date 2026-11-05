
def caucionar_dias():
    import os
    import pandas as pd

    dias = int(input("Ingrese la cantidad de días para la caución: "))
    monto_inicial = float(input("Ingrese el capital inicial a colocar: "))

    tasa_anual = 0.40 

    monto_final = monto_inicial * (1 + (tasa_anual * dias / 365))

    archivo_csv = "historial_cauciones.csv"
    nuevo_registro = pd.DataFrame({'dias': [dias], 'capital_inicial': [monto_inicial], 'monto_obtenido': [monto_final]})

    if os.path.exists(archivo_csv):
        df_existente = pd.read_csv(archivo_csv)
        df_actualizado = pd.concat([df_existente, nuevo_registro], ignore_index=True)
    else:
        df_actualizado = nuevo_registro

    df_actualizado.to_csv(archivo_csv, index=False)
    print(f"Operación registrada. Plazo: {dias} días | Monto final estimado: {monto_final:.2f}")
    
    

caucionar_dias