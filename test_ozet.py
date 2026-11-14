import unittest
from ozet import en_sik_hatalar, satirlari_ayristir, seviye_sayilari

class AyristirmaTesti(unittest.TestCase):
    def test_satirlari_ayristirir_ve_sayar(self):
        satirlar = [
            "2026-11-14 10:00:01 [INFO] uygulama başladı",
            "2026-11-14 10:00:05 [ERROR] bağlantı koptu",
            "bozuk satır",
            "2026-11-14 10:01:00 [info] istek alındı",
        ]
        kayitlar = satirlari_ayristir(satirlar)
        self.assertEqual(len(kayitlar), 3)
        self.assertEqual(seviye_sayilari(kayitlar), {"INFO": 2, "ERROR": 1})

class HataTesti(unittest.TestCase):
    def test_en_sik_hatayi_bulur(self):
        kayitlar = [
            {"zaman": "", "seviye": "ERROR", "mesaj": "bağlantı koptu"},
            {"zaman": "", "seviye": "ERROR", "mesaj": "bağlantı koptu"},
            {"zaman": "", "seviye": "ERROR", "mesaj": "disk dolu"},
            {"zaman": "", "seviye": "INFO", "mesaj": "başladı"},
        ]
        self.assertEqual(en_sik_hatalar(kayitlar, 1), [("bağlantı koptu", 2)])


if __name__ == "__main__":
    unittest.main()