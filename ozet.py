import re

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