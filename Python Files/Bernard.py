import speech_recognition as sr
import time
import sys
from commands import Komut

r = sr.Recognizer()
        
Komut.kayit_ol()
hitap = Komut.kayit_ol()[2]

c = 0

while True:

    with sr.Microphone() as source:
        time.sleep(1)

        if c == 0:

            z = "Merhaba, hoş geldin."
            print("Bernard: " + z)
            Komut.konus(z)

            x = "Gerçekleştirmemi istediğin bir komut var mı "
            y = "? Komut listeme ulaşmak için 'komut say' demelisin."
            print("Bernard: " + x + hitap + y)
            Komut.konus(x + " " + hitap + y)
            ses = r.listen(source)
            c += 1
            
        else:
            x = "Gerçekleştirmemi istediğin bir komut var mı"
            print("Bernard: " + x + " " + hitap + "?")
            Komut.konus(x + hitap + "?")
            ses = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(ses, language="tr-tr")
        data = data.capitalize()
        print(str(hitap) + ": " + data)
        time.sleep(3)
        Komut.komut_bul(data)

    except sr.UnknownValueError:
        print("Bernard: Özür dilerim " + hitap + ". Ne dediğini anlayamadım, tekrar edebilir misin?" )
        Komut.konus("Özür dilerim " + hitap + ". Ne dediğini anlayamadım, tekrar edebilir misin?" )
        