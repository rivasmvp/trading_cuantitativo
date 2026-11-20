import time
import pandas as pd
import yfinance as yf

commodities_sectoriales = [
            'XLE', 'XLB', 'XLU', 'XME', 'GDX', 'GLD', 'SLV', 'USO', 'DBC', 'DBA', 'COPX', 'URA', 
            'XLI', 'XLF', 'XLRE', 'XLY', 'XLV', 'XBI', 'XLC', 'XLK', 'SMH', 'XLP', 'CIBR', 'IBB', 
            'ICLN', 'ARKK', 'UNG'
        ]

indices_etfs = [
            'SPY', 'SPXL', 'TQQQ', 'QQQ', 'DIA', 'IWM', 'EEM', 'EWJ', 'VOO', 'VTI', 'EFA', 'VNQ'
        ]

commodities_sectoriales = [
        'XLE', 'XLB', 'XLU', 'XME', 'GDX', 'GLD', 'SLV', 'USO', 'DBC', 'DBA', 'COPX', 'URA', 
        'XLI', 'XLF', 'XLRE', 'XLY', 'XLV', 'XBI', 'XLC', 'XLK', 'SMH', 'XLP', 'CIBR', 'IBB', 
        'ICLN', 'ARKK', 'UNG'
    ]

renta_fija = [
        'TLT', 'IEF', 'LQD', 'HYG'
    ]

tech_semis = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'AMD', 'INTC', 'QCOM', 'AVGO', 'IBM', 
        'ORCL', 'CRM', 'ADBE', 'NOW', 'SNOW', 'PLTR', 'UBER', 'ABNB', 'SHOP', 'MELI', 'PYPL', 
        'COIN', 'ROKU', 'NET', 'TEAM', 'DDOG', 'ZS', 'CRWD', 'ANET', 'PANW', 'AMAT', 
        'LRCX', 'MU', 'TXN', 'ADI', 'MRVL', 'ASML', 'ARM', 'TSM', 'ENPH', 'FSLR', 'CDNS', 
        'SNPS', 'KLAC', 'NXPI', 'STM', 'ON', 'DELL', 'HPQ', 'WDC', 'BTC-USD'
    ]

consumo_autos = [
        'TSLA', 'NIO', 'XPEV', 'LI', 'RIVN', 'LCID', 'F', 'GM', 'TM', 'HMC', 'KO', 'PEP', 
        'MCD', 'SBUX', 'NKE', 'DIS', 'NFLX', 'WMT', 'TGT', 'COST', 'PG', 'CL', 'MO', 'PM', 
        'BTI', 'YUM', 'CMG', 'MAR', 'HLT', 'BKNG', 'EXPE', 'EBAY', 'ETSY', 'JD', 'BABA', 
        'PDD', 'BIDU', 'MDLZ', 'KHC', 'KDP', 'GIS', 'TJX'
    ]

salud = [
        'JNJ', 'PFE', 'MRK', 'ABBV', 'LLY', 'NVO', 'AZN', 'AMGN', 'GILD', 'BMY', 'CVS', 
        'UNH', 'ELV', 'ISRG', 'MDT', 'BSX', 'ZTS', 'SYK', 'TMO', 'DHR', 'ABT', 'EW', 'VRTX'
    ]

energia = [
        'XOM', 'CVX', 'COP', 'SLB', 'HAL', 'BKR', 'OXY', 'VIST', 'PBR', 'TTE', 'BP', 'SHEL', 
        'ENB', 'TRP', 'EQNR', 'SU', 'EOG', 'DVN', 'FANG', 'VLO', 'MPC', 'KMI', 'OKE'
    ]

banca = [
        'JPM', 'BAC', 'WFC', 'C', 'GS', 'MS', 'BLK', 'SCHW', 'AXP', 'V', 'MA', 'COF', 
        'USB', 'PNC', 'TFC', 'SPGI', 'MCO', 'AIG', 'MET', 'PRU', 'TRV', 'BRK-B'
    ]

industria = [
        'BA', 'LMT', 'RTX', 'NOC', 'GD', 'CAT', 'DE', 'HON', 'GE', 'MMM', 'UPS', 'FDX', 
        'UNP', 'CSX', 'NSC', 'WM', 'EMR', 'ETN', 'PH', 'ITW', 'GEV', 'ACN'
    ]

mineria_materials = [
        'RIO', 'BHP', 'VALE', 'FCX', 'SCCO', 'NEM', 'GOLD', 'AEM', 'PAAS', 'AA', 'CLF', 
        'NUE', 'STLD', 'APD', 'SHW', 'ECL', 'DOW', 'DD', 'CCJ', 'TECK', 'TX', 'ADM', 'BG', 
        'MOS', 'CTVA', 'LIN'
    ]

utilities_reits = [
        'NEE', 'DUK', 'SO', 'D', 'AEP', 'EXC', 'SRE', 'PCG', 'PEG', 'VZ', 'T', 'TMUS', 
        'CHTR', 'CMCSA', 'VOD', 'AMX', 'BCE', 'ED', 'PLD', 'AMT'
    ]

import time
import pandas as pd
import yfinance as yf


def get_vix(temporalidad: str = "1d", periodo: str = "1y") -> pd.DataFrame:
    """
    Descarga datos históricos del índice VIX (^VIX) usando yfinance.

    Parámetros:
        temporalidad: intervalo de barras (ej. "60m", "1d", "1wk").
        periodo: ventana histórica (ej. "1mo", "6mo", "1y", "5y").
    """
    t0 = time.perf_counter()
    ticker = "^VIX"

    df_vix = yf.download(
        tickers=ticker,
        interval=temporalidad,
        period=periodo,
        auto_adjust=True,
        progress=False,
        threads=False,
    )

    if df_vix is None or df_vix.empty:
        print(f"Advertencia: no se obtuvieron datos para {ticker} ({temporalidad}, {periodo}).")
        return pd.DataFrame()

    if isinstance(df_vix.columns, pd.MultiIndex):
        if ticker in df_vix.columns.get_level_values(-1):
            df_vix = df_vix.xs(ticker, axis=1, level=-1)
        elif ticker in df_vix.columns.get_level_values(0):
            df_vix = df_vix.xs(ticker, axis=1, level=0)
        else:
            df_vix.columns = df_vix.columns.get_level_values(0)

    df_vix = df_vix.dropna(how="all").sort_index()
    elapsed = time.perf_counter() - t0
    print(f"Datos del VIX descargados en {elapsed:.2f} segundos.")
    return df_vix

def get_sectores():
    sectores = (commodities_sectoriales)
    return sectores

def scrapear_tickers():
    
    # --- UNIVERSO DE CEDEARS Y ETFS POR SECTOR ---
    # --- UNIFICA LAS LISTAS ---
    mis_tickers = (
        indices_etfs + commodities_sectoriales + renta_fija + 
        tech_semis + consumo_autos + salud + energia + 
        banca + industria + mineria_materials + utilities_reits
    )

    if mis_tickers:
        print(f"Se han cargado {len(mis_tickers)} tickers...")
        
    return mis_tickers