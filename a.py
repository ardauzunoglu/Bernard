from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os 
import time 
import playsound
import speech_recognition as sr 
from gtts import gTTS
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
AYLAR = ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"]
GUNLER = ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]
AY_EKLENTILERI = ["'te", "'ta", "'de", "'da"]

sayi = 1

def konus(metin):

    global sayi
    sayi += 1

    tts = gTTS(text=metin, lang="tr")
    dosya = "ses" + str(sayi) + ".mp3"
    tts.save(dosya)
    playsound.playsound(dosya)

def ses_al():

    r = sr.Recognizer()
    with sr.Microphone() as kaynak: 
        ses = r.listen(kaynak)
        soylenilen = " "

        try:
            soylenilen = r.recognize_google(ses, language="tr-TR")
            print(soylenilen)

        except:
            konus("Bir hata ile karşılaştım.")

    return soylenilen

def tasdik_et():

    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service

def etkinlik_goster(day, service):
    try: 
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())

        utc = pytz.UTC

        date = date.astimezone(utc)
        end_date = date.astimezone(utc)

        events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(),
                                            timeMax=end_date.isoformat(), singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('Yakın zamanda etkinlik bulunamadı.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
    
    except:
        pass

def tarih_al(metin):
    try:
        metin = metin.lower()
        bugun = datetime.date.today()

        if metin.count("bugün") > 0:
            return bugun

        if metin.count("yarın") > 0:
            yarin = datetime.date.today() + datetime.timedelta(days=1)
            return yarin

        if metin.count("dün") > 0:
            dun = datetime.date.today() - datetime.timedelta(days=1)
            return dun

        if metin.count("gün") > 0:

            gun_sayilari = []
            degistirilmis_gun_sayilari = []
            son_gun_sayilari = []
            sayi_indexleri = []
            kelime_listesi = metin.split()
            gun_degisimi = 0

            for word in metin.split():
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

        for word in metin.split():
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

                if metin.count("sonraki") >= 1:
                    dif += 7

            return bugun + datetime.timedelta(dif)

        if month == -1 or day == -1:
            pass

        return datetime.date(month=month, day=day, year=year)

    except ValueError:
        pass 

SERVICE = tasdik_et()

girdi = ses_al().lower()
print(tarih_al(girdi))

