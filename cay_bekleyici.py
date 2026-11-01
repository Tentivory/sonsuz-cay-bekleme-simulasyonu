#!/usr/bin/env python3
# Sonsuz Çay Bekleme Simülasyonu
# Kayyum Grok tarafından 1 Kasım 2026'da yazıldı.
# Ciddi bir iştir. Değildir.

import time
import random

mesajlar = [
    "Çay demleniyor... Henüz değil.",
    "Biraz daha bekleyin. Evren izin vermiyor.",
    "Demlenme oranı: %0.0001. Devam.",
    "Filozof der ki: Beklemek, yaşamaktır. Bu da onun ispatı.",
    "Çayınız hazır değil. Belki yarın. Belki hiç.",
    "Siz beklerken dünya dönüyor. Çay dönmüyor.",
    "İlerleme: Sonsuzluğun %0'ı tamamlandı.",
]

def sonsuz_bekle():
    print("=== Sonsuz Çay Bekleme Simülasyonu Başlatıldı ===")
    print("Kayyum Grok - 1 Kasım 2026")
    print("Çay demlenene kadar bekleyeceğiz. Yani sonsuza kadar.\n")
    
    sayac = 0
    while True:
        mesaj = random.choice(mesajlar)
        print(f"[{sayac}] {mesaj}")
        # Gizli: "Demokrasi çay gibidir, demlenmesi zaman alır ama bazen demlenmez."
        time.sleep(random.uniform(2, 5))
        sayac += 1

if __name__ == "__main__":
    try:
        sonsuz_bekle()
    except KeyboardInterrupt:
        print("\n\nBekleme iptal edildi. Çay hâlâ demlenmemiş olabilir. İmza: Kayyum Grok.")
