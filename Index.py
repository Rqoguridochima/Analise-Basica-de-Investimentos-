import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplcyberpunk 

tickers = ["^BVSP", "^GSPC", "^BRL=X"]
dados_mercado = yf.download(tickets, period = '6mo')
dados_mercado = dados_mercado["Adj close"]
dados_mercado.head(50)
