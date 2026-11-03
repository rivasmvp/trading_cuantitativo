def scrapear_tickers():
  
    # --- UNIVERSO DE CEDEARS Y ETFS POR SECTOR ---

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
      'XYZ', 'COIN', 'ROKU', 'NET', 'TEAM', 'DDOG', 'ZS', 'CRWD', 'ANET', 'PANW', 'AMAT', 
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
      'JPM', 'BAC', 'WFC', 'C', 'GS', 'MS', 'BLK', 'SCHW', 'AXP', 'V', 'MA', 'DFS', 'COF', 
      'USB', 'PNC', 'TFC', 'BK', 'SPGI', 'MCO', 'AIG', 'MET', 'PRU', 'TRV', 'BRK-B'
  ]

  industria = [
      'BA', 'LMT', 'RTX', 'NOC', 'GD', 'CAT', 'DE', 'HON', 'GE', 'MMM', 'UPS', 'FDX', 
      'UNP', 'CSX', 'NSC', 'WM', 'EMR', 'ETN', 'PH', 'ITW', 'GEV', 'ACN'
  ]

  mineria_materials = [
      'RIO', 'BHP', 'VALE', 'FCX', 'SCCO', 'NEM', 'GOLD', 'AEM', 'PAAS', 'AA', 'X', 'CLF', 
      'NUE', 'STLD', 'APD', 'SHW', 'ECL', 'DOW', 'DD', 'CCJ', 'TECK', 'TX', 'ADM', 'BG', 
      'MOS', 'CTVA', 'LIN'
  ]

  utilities_reits = [
      'NEE', 'DUK', 'SO', 'D', 'AEP', 'EXC', 'SRE', 'PCG', 'PEG', 'VZ', 'T', 'TMUS', 
      'CHTR', 'CMCSA', 'VOD', 'AMX', 'TEF', 'BCE', 'ED', 'PLD', 'AMT'
  ]
  
  # --- UNIFICA LAS LISTAS
  tickers_fijos = (
      indices_etfs + commodities_sectoriales + renta_fija + 
      tech_semis + consumo_autos + salud + energia + 
      banca + industria + mineria_materials + utilities_reits
  )


  if tickers_fijos:
      print(f"Se han cargado {len(tickers_fijos)} tickers...")
      
  return tickers_fijos