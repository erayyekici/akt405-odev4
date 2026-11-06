# AKT405 - Aktüeryal Yazılımlar Ödev 4

Bu çalışma USD/TRY döviz kuru, ABD Hazine bonosuna bağlı iShares 20+ Year Treasury Bond ETF (TLT) ve Koç Holding hissesi (KCHOL.IS) için günlük piyasa verileri ve getiri/risk ölçülerini analiz eder.

## Seçilen varlıklar

| Çalışma adı | Yahoo Finance sembolü | Tür |
|---|---|---|
| USD_TRY | TRY=X | Dolar/Türk Lirası kuru |
| ABD_BONO_TLT | TLT | ABD tahvil ETF'i (bono temsili) |
| KOC_HOLDING | KCHOL.IS | BIST hisse |

Semboller Yahoo Finance üzerinden doğrulanmıştır. Veri aralığı: **01.01.2021–31.12.2025**.

## Sanal ortam ve kurulum

Windows PowerShell'de proje klasöründe aşağıdaki komutları çalıştırın:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Çalıştırma sırası

1. Veriyi indirip ortak işlem günlerine indirir ve `kapanis.csv` oluşturur:
   ```powershell
   python cek_veri.py
   ```
2. Getiri/risk tablosu ile korelasyon matrisini yazdırır ve `fiyatlar.png` oluşturur:
   ```powershell
   python analiz.py
   ```

## Çeşitlendirme yorumu

Günlük basit getirilerde en düşük korelasyon **ABD_BONO_TLT ile KOC_HOLDING** arasında bulunmuştur (−0,0894). Bu hafif negatif ilişki, TLT'nin fiyat hareketleri yükselirken Koç Holding'in hareketinin genellikle ters yönde olma eğiliminde olduğunu gösterir ve daha iyi çeşitlendirme potansiyeli sağlar. Bu nedenle bu iki varlık aynı portföyde birlikte kullanıldığında tek bir varlığa göre dalgalanmalar daha iyi dengeleyebilir.

## Veri çekilme tarihi

Veri **06.11.2026** tarihinde Yahoo Finance üzerinden yfinance ile çekildi.

## Yapay zekâ kullanımı

Projenin Python betiklerinin iskeletinin oluşturulması, Yahoo Finance veri indirme formatlarının uyarlanması ve hata kontrollerinin hazırlanması amacıyla yapay zekâ asistanından yardım alınmıştır. Hesaplar ve çıktıların doğruluğu çalıştırılarak kontrol edilmiştir.
