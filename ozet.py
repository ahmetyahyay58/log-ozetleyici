import re
import sys
from collections import Counter

# Beklenen biçim: 2026-11-14 10:00:01 [ERROR] mesaj
SATIR = re.compile(r"^(\S+ \S+) \[(\w+)\] (.*)$")


def satirlari_ayristir(satirlar):
    """Log satırlarını sözlüğe çevirir, biçime uymayan satırları atlar."""
    kayitlar = []
    for satir in satirlar:
        eslesme = SATIR.match(satir.strip())
        if eslesme:
            zaman, seviye, mesaj = eslesme.groups()
            kayitlar.append({"zaman": zaman, "seviye": seviye.upper(), "mesaj": mesaj})
    return kayitlar


def seviye_sayilari(kayitlar):
    """Her seviyeden (INFO, ERROR...) kaç kayıt olduğunu döndürür."""
    sonuc = {}
    for kayit in kayitlar:
        sonuc[kayit["seviye"]] = sonuc.get(kayit["seviye"], 0) + 1
    return sonuc



def en_sik_hatalar(kayitlar, n=3):
    """En sık tekrarlanan ERROR mesajlarını ve kaç kez geçtiklerini döndürür."""
    hatalar = Counter(k["mesaj"] for k in kayitlar if k["seviye"] == "ERROR")
    return hatalar.most_common(n)



def main():
    if len(sys.argv) != 2:
        print("Kullanım: py ozet.py dosya.log")
        return
    with open(sys.argv[1], encoding="utf-8") as dosya:
        kayitlar = satirlari_ayristir(dosya)
    print(f"Toplam kayıt: {len(kayitlar)}")
    for seviye, sayi in seviye_sayilari(kayitlar).items():
        print(f"  {seviye}: {sayi}")
    print("En sık hatalar:")
    for mesaj, sayi in en_sik_hatalar(kayitlar):
        print(f"  {sayi} kez: {mesaj}")


if __name__ == "__main__":
    main()