import os
import pandas as pd
import requests

def obtener_tasa_por_plazo(dias_solicitados):
    try:
        url = "https://api.argentinadatos.com/v1/finanzas/cauciones/ars/ultimo"
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            tasa_porcentaje = datos.get('tasa', datos.get('tasaPromedio', 0))
            if tasa_porcentaje > 0:
                return tasa_porcentaje / 100.0
    except Exception:
        pass
    
    try:
        url_historico = "https://api.argentinadatos.com/v1/finanzas/cauciones/ars"
        respuesta = requests.get(url_historico, timeout=5)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            for item in reversed(datos):
                if int(item.get('dias', 0)) == dias_solicitados:
                    return float(item.get('tasa', 0)) / 100.0
            if datos:
                return float(datos[-1].get('tasa', 26.10)) / 100.0
    except Exception:
        pass

    return 0.2610

def caucionar():
    monto_inicial = float(input("ingrese cantidad a caucionar: "))
    dias = int(input("Ingrese la cantidad de días para la caución: "))
    
    tasa_anual = obtener_tasa_por_plazo(dias)
    monto_final = monto_inicial * (1 + (tasa_anual * dias / 365))
    ganancia = monto_final - monto_inicial
    
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    archivo_csv = os.path.join(directorio_script, "historial_cauciones.csv")
    
    nuevo_registro = pd.DataFrame({
        'dias': [dias], 
        'capital_inicial': [monto_inicial], 
        'tasa_anual': [tasa_anual],
        'monto_obtenido': [monto_final]
    })
    
    if os.path.exists(archivo_csv):
        df_existente = pd.read_csv(archivo_csv)
        df_actualizado = pd.concat([df_existente, nuevo_registro], ignore_index=True)
    else:
        df_actualizado = nuevo_registro
        
    df_actualizado.to_csv(archivo_csv, index=False)
    
    suma_acumulada = df_actualizado['monto_obtenido'].sum()
    
    print(f"Plazo: {dias} días | TNA Aplicada: {tasa_anual * 100:.2f}% | Monto Final: ${monto_final:.2f} | Ganancia: ${ganancia:.2f}")
    print(f"Suma total acumulada en historial: ${suma_acumulada:.2f}")

if __name__ == "__main__":
    caucionar()