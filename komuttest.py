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
import sqlite3 
from gtts import gTTS
from  subcommands import tarih_bul
import pytz
from commands import Komut
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

r = sr.Recognizer()

c = 0

def google_giris():

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

def gun_sayisi_al():

    x = "Kaç gün içerisindeki etkinlikleri görmek istiyorsunuz?"
    print("Bernard: " + x)
    Komut.konus(x)


    with sr.Microphone() as source:
        ses = r.listen(source)

    gun_sayisi = 0

    try:
        gun_sayisi = r.recognize_google(ses, language="tr-tr")
        gun_sayisi = int(gun_sayisi)

    except sr.UnknownValueError:
        x = "Ne dediğini anlayamadım. Lütfen komutu tekrar çağır."
        print("Bernard: " + x)
        Komut.konus(x)

    return gun_sayisi

def etkinlik_goster(gun_sayisi, service):

    simdi = datetime.datetime.utcnow().isoformat() + "Z"
    x = "{} gün içerisindeki etkinlikler getiriliyor.".format(gun_sayisi)
    print("Bernard: " + x)
    Komut.konus(x)
    
    time.sleep(3)

    etkinlik_sonuclari = service.events().list(calendarId = "primary", timeMin=simdi, maxResults=gun_sayisi,
                                                singleEvents=True, orderBy="startTime").execute()

    etkinlikler = etkinlik_sonuclari.get("items", [])

    if not etkinlikler:
        x = "{} gün içerisinde herhangi bir etkinlik yok.".format(gun_sayisi)
        print("Bernard: " + x)
        Komut.konus(x)
    for etkinlik in etkinlikler:
        baslangic = etkinlik["start"].get("dateTime", etkinlik["start"].get("date"))

