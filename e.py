import speech_recognition as sr
import time
import sys
import sqlite3
from commands import Komut

gerekli_platformlar = ["Netflix", "Spotify"]

Komut.tablo_olustur()

with sqlite3.connect("hesap_bilgileri.db") as db:
    cursor = db.cursor()
    platformlar = [Platform[0] for Platform in cursor.execute("SELECT Platform from HesapBilgileri")]

    i = 0

    if (len(platformlar) == 0):    
        Komut.bilgi_ver()

    elif (0 < len(platformlar) < len(gerekli_platformlar)):
        while i < len(gerekli_platformlar):
            if (gerekli_platformlar[i] == platformlar[i]):
                i += 1

            else:
                Komut.bilgi_ver()

    else:
        print("Oyna devam")





    """if (len(gerekli_platformlar) == len(platformlar)):
        
        while i < len(gerekli_platformlar):

            if (gerekli_platformlar[0] == platformlar[0]):

                i += 1
        
            else:
                Komut.bilgi_ver()"""
            