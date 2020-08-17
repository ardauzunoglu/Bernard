import speech_recognition as sr
import time
import sys
from commands import Komut

r = sr.Recognizer()

i = 0

hitap = ""

def komut_bul(data):

    if data.upper() == "KAPAT":
        sys.exit()

    elif data.upper() == "KOMUT SAY":
        Komut.komut_say()

    elif data.upper() == "KOMUTLARINI SAY":
        Komut.komut_say()

    elif data.upper() == "KOMUTLARINI SAYABİLİRSİN":
        Komut.komut_say()

    elif data.upper() == "KOMUTLARINI SÖYLE":
        Komut.komut_say()

    elif data.upper() == "KOMUTLARINI SÖYLEYEBİLİRSİN":
        Komut.komut_say()

    else:
        x = "Üzgünüm, geçersiz komut."
        print("Bernard: " + x)
        Komut.konus(x)


def hitap_et():
    sor = "Size nasıl hitap etmeliyim?"
    print("Bernard: " + sor)
    Komut.konus(sor)
    with sr.Microphone() as source:
        ses = r.listen(source)

    try:
        global hitap 

        hitap = r.recognize_google(ses, language="tr-tr")
        hitap = hitap.capitalize()
        print(hitap + ": " + hitap)
        hitap = hitap

    except sr.UnknownValueError:
        print("Bernard: Özür dilerim. Ne dediğini anlayamadığım için sana Kullanıcı olarak hitap edeceğim, tekrar denemek için uygulamayı kapatıp açabilirsin." )
        Komut.konus("Özür dilerim. Ne dediğini anlayamadığım için sana Kullanıcı olarak hitap edeceğim, tekrar denemek için uygulamayı kapatıp açabilirsin." )

        hitap = "Kullanıcı"


if i == 0:
    hitap_et()
    i += 1

while True:
    with sr.Microphone() as source:
        time.sleep(1)
        print("Bernard: Senin için ne yapabilirim " + hitap + "?")
        Komut.konus("Senin için ne yapabilirim " + hitap + "?")
        ses = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(ses, language="tr-tr")
        data = data.capitalize()
        print(str(hitap) + ": " + data)
        time.sleep(3)
        komut_bul(data)

    except sr.UnknownValueError:
        print("Bernard: Özür dilerim " + hitap + ". Ne dediğini anlayamadım, tekrar edebilir misin?" )
        Komut.konus("Özür dilerim " + hitap + ". Ne dediğini anlayamadım, tekrar edebilir misin?" )
        