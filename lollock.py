import pyautogui
import time

# DERECELİ TEK ÇİFTE KADAR SEÇME 

#X:  308 Y:  108 RGB: ( 23,  47,  60) OYNA
#X:  297 Y:  727 RGB: ( 10,  27,  34) DERECELİ TEK/ÇİFT SEÇ
#X:  830 Y:  919 RGB: (193, 190, 178) ONAYLA
#X:  804 Y:  914 RGB: (184, 187, 188) BAŞLAT

# LANE POZİSYONLARI
#SOLO - X:  803 Y:  841 RGB: (189, 181, 153)
#JUNGLE - X:  921 Y:  847 RGB: ( 94, 108, 107)
#MID - X:  932 Y:  837 RGB: ( 13,  49,  60)
#ADC - X: 1000 Y:  841 RGB: (114, 129, 124)
#SUP - X: 1078 Y:  843 RGB: (172, 161, 129)
#DOLDUR - X: 1078 Y:  843 RGB: (172, 161, 129)

#X:  981 Y:  914 RGB: ( 40,  48,  52) BİRİNCİ LANE SEÇME SLOTU
#X: 1029 Y:  910 RGB: (170, 187, 182) İKİNCİ LANE SEÇME SLOTU

# KARŞILAŞMA BULUNDU RGB KODU (KORECE İÇİN)
# X:  833 Y:  544 RGB: ( 12,  12,  12)
# X: 1107 Y:  546 RGB: ( 12,  12,  12) ikinci offset

# KARŞILAŞMA KABUL ETME BUTONU
# X:  955 Y:  758 RGB: ( 40,  40,  40)


time.sleep(2) # 2 saniye bekle

# Dereceli Seç

pyautogui.click(308, 108) # oyna tuşuna bastı
time.sleep(3) # 3 saniye bekle
pyautogui.click(297, 727) # dereceli tek çift seçti
time.sleep(3) # 3 saniye bekle
pyautogui.click(830, 919) # onayladı
time.sleep(3) # 3 saniye bekle

# Lane Seç
pyautogui.click(981, 914) # 1. slot seçildi
time.sleep(2)
pyautogui.click(932, 837) # mid lane seçildi
time.sleep(2)
pyautogui.click(1029, 910) # 2. slot seçildi
time.sleep(2)
pyautogui.click(921, 847) # jungle lane seçildi
time.sleep(2)

# Başlat

pyautogui.click(804, 914)

# Karşılaşma Bulundu



while True: # bulana kadar loop
    
    ss = pyautogui.screenshot() 
    lost_ = ss.getpixel((1107, 546)) # Karşılaşma bulundu yazısının rgb kodlarını almak için kullandığımız kod
    lost__ = ss.getpixel((833, 544)) # Karşılaşma bulundu yazısının rgb kodlarını almak için kullandığımız kod (yedek)

    if lost__ == (240, 230, 210) and lost_ == (240, 230, 210):
        time.sleep(3) #buga girmemesi adına 3 saniye bekliyoruz
        pyautogui.click(955, 758)
        print("Karşılaşma Bulundu ve Kabul Edildi! Konsol 5 saniye sonra kendini kapatacak.")
        time.sleep(5)
        exit()
    else: 
        print("Bulunamadı")
        time.sleep(1)

# Kaynaklar:
# https://stackoverflow.com/questions/44533241/how-to-print-out-live-mouse-position-coordinates-using-pyautogui
# https://stackoverflow.com/questions/64722136/how-to-use-pyautogui-to-detect-rgb-values
# https://pyautogui.readthedocs.io/en/latest/
