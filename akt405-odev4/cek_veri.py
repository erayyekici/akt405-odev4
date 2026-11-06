from pathlib import Path

import pandas as pd
import yfinance as yf

START_DATE = "2021-01-01"
END_DATE = "2026-01-01"
SYMBOLS = {
    "USD_TRY": "TRY=X",
    "ABD_BONO_TLT": "TLT",
    "KOC_HOLDING": "KCHOL.IS",
}
OUTPUT_FILE = Path(__file__).resolve().parent / "kapanis.csv"


def download_close(symbol: str) -> pd.Series:
    data = yf.download(
        symbol,
        start=START_DATE,
        end=END_DATE,
        progress=False,
        auto_adjust=True,
        actions=False,
    )
    if data.empty:
        raise RuntimeError(f"Yahoo Finance '{symbol}' için veri getirmedi.")

    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close = close.rename(symbol)
    close.index = pd.to_datetime(close.index).tz_localize(None)
    return close


def main() -> None:
    frames = [download_close(symbol) for symbol in SYMBOLS.values()]
    prices = pd.concat(frames, axis=1, join="inner")
    prices.columns = list(SYMBOLS.keys())
    prices = prices.dropna()
    if prices.empty:
        raise RuntimeError("Ortak işlem gününde veri bulunamadı.")

    prices.to_csv(OUTPUT_FILE, index_label="Date")
    print(f"Ortak işlem günü gözlem sayısı: {len(prices)}")
    print(prices.tail())


if __name__ == "__main__":
    main()
