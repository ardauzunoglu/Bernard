from __future__ import print_function
import datetime
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os 
import time 
import playsound
import speech_recognition as sr 
from gtts import gTTS
import pytz

r = sr.Recognizer()
sayi = 0

def tarih_bul(tarih):
        AYLAR = ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"]
        GUNLER = ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]
        AY_EKLENTILERI = ["'te", "'ta", "'de", "'da"]

        try:
            tarih = tarih.lower()
            bugun = datetime.date.today()

            if tarih.count("bugün") > 0:
                return bugun

            if tarih.count("yarın") > 0:
                yarin = datetime.date.today() + datetime.timedelta(days=1)
                return yarin

            if tarih.count("dün") > 0:
                dun = datetime.date.today() - datetime.timedelta(days=1)
                return dun

            if tarih.count("gün") > 0:

                gun_sayilari = []
                degistirilmis_gun_sayilari = []
                son_gun_sayilari = []
                sayi_indexleri = []
                kelime_listesi = tarih.split()
                gun_degisimi = 0

                for word in tarih.split():
                    if word.isdigit():
                        gun_sayilari.append(int(word))

                for i in gun_sayilari:
                    sayi_indexi = kelime_listesi.index(str(i))
                    sayi_indexleri.append(sayi_indexi)

                for i in sayi_indexleri:
                    x = 0
                    try:
                        while x<=len(kelime_listesi):
                            j = i + x
                            if kelime_listesi[j] == "önce" or "sonra":
                                if kelime_listesi[j] == "önce":
                                    sayi = int(kelime_listesi[i])
                                    degistirilmis_gun_sayilari.append(-sayi)

                                x += 1

                                if kelime_listesi[j] == "sonra":
                                    sayi = int(kelime_listesi[i])
                                    degistirilmis_gun_sayilari.append(sayi)

                                x += 1

                            else:
                                x += 1
                    except IndexError:
                        pass

                for i in degistirilmis_gun_sayilari:
                    if i not in son_gun_sayilari:
                        son_gun_sayilari.append(i)       

                for i in son_gun_sayilari:
                    gun_degisimi += i

                tarih = datetime.date.today() + datetime.timedelta(days=gun_degisimi)
                return tarih 

            day = -1
            day_of_week = -1
            month = -1
            year = bugun.year 

            for word in tarih.split():
                if word in AYLAR:
                    month = AYLAR.index(word) + 1 

                elif word in GUNLER:
                    day_of_week = GUNLER.index(word)

                elif word.isdigit():
                    day = int(word)

                else:
                    for ek in AY_EKLENTILERI:
                        found = word.find(ek)
                        if found > 0:
                            try:
                                month = word[:found]

                                if month.lower() == "ocak":
                                    month = 1

                                elif month.lower() == "şubat":
                                    month = 2

                                elif month.lower() == "mart":
                                    month = 3

                                elif month.lower() == "nisan":
                                    month = 4

                                elif month.lower() == "mayıs":
                                    month = 5

                                elif month.lower() == "haziran":
                                    month = 6

                                elif month.lower() == "temmuz":
                                    month = 7

                                elif month.lower() == "ağustos":
                                    month = 8

                                elif month.lower() == "eylül":
                                    month = 9

                                elif month.lower() == "ekim":
                                    month = 10

                                elif month.lower() == "kasım":
                                    month = 11

                                elif month.lower() == "aralık":
                                    month = 12


                            except:
                                pass
                    
            if month < bugun.month and month != -1:
                year = year + 1

            if day < bugun.day and month == -1 and day != -1:
                month = month + 1

            if month == -1 and day == -1 and day_of_week != -1:
                current_day_of_week = bugun.weekday()
                dif = day_of_week - current_day_of_week

                if dif <= 0:
                    dif += 7

                    if tarih.count("sonraki") >= 1:
                        dif += 7

                return bugun + datetime.timedelta(dif)

            if month == -1 or day == -1:
                pass

            return datetime.date(month=month, day=day, year=year)

        except ValueError:
            pass
