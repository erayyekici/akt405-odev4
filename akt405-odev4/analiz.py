from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "kapanis.csv"
PLOT_FILE = Path(__file__).resolve().parent / "fiyatlar.png"
TRADING_DAYS = 252

prices = pd.read_csv(DATA_FILE, index_col="Date", parse_dates=True)
simple_returns = prices.pct_change(fill_method=None).dropna(how="all")
log_returns = np.log(prices / prices.shift(1)).dropna()

annual_return = TRADING_DAYS * log_returns.mean()
annual_volatility = log_returns.std(ddof=1) * np.sqrt(TRADING_DAYS)
risk_table = pd.DataFrame({
    "Yıllık Ortalama Getiri": annual_return,
    "Yıllık Oynaklık": annual_volatility,
})

print("Yıllık getiri ve risk tablosu:")
print(risk_table.to_string(float_format=lambda x: f"{x:.6%}"))
print("\nSeçilen varlık için PT/P0 - 1 ve logaritmik toplam getiri:")
asset = prices.columns[0]
price_method = prices[asset].iloc[-1] / prices[asset].iloc[0] - 1
log_method = np.exp(log_returns[asset].sum()) - 1
print(f"{asset} PT/P0 - 1:                  {price_method:.6%}")
print(f"{asset} exp(toplam log-getiri)-1: {log_method:.6%}")
print(f"Fark:                             {price_method - log_method:.12%}")

indexed_prices = prices / prices.iloc[0] * 100
ax = indexed_prices.plot(figsize=(12, 6))
ax.set_title("Dolar/TRY, ABD Bonosu ve Koç Holding Endeksli Fiyatlar (Başlangıç=100)")
ax.set_xlabel("Tarih")
ax.set_ylabel("Endeksli Fiyat (Başlangıç = 100)")
ax.legend(title="Varlık", loc="best")
plt.tight_layout()
plt.savefig(PLOT_FILE, dpi=150)
plt.close()
print(f"\nGrafik kaydedildi: {PLOT_FILE.name}")

print("\nGünlük basit getiri korelasyon matrisi:")
print(simple_returns.corr().to_string(float_format=lambda x: f"{x:.4f}"))
