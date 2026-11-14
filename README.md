# log-ozetleyici

Log dosyalarındaki kayıtları seviyelerine göre sayan ve en sık hataları bulan küçük bir Python aracı.

## Kullanım

    py ozet.py ornek.log

Beklenen satır biçimi: `2026-11-14 10:00:01 [ERROR] mesaj`. Bu biçime uymayan satırlar atlanır.

## Test

    py -m unittest