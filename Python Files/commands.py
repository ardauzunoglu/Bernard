import datetime
import pickle
import os.path
import datetime
import sys
import speedtest
import os 
import time 
import playsound
import speech_recognition as sr
import sqlite3 
import pytz
import smtplib
import requests
import wikipedia
import pyqrcode
from __future__ import print_function
from win10toast import ToastNotifier
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import date
from gtts import gTTS
from subcommands import tarih_bul, json_getir_bugun, kelvin_donusturucu
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from smtplib import SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

r = sr.Recognizer()
sayi = 1
e = 0

class Komut():
    ##KOMUTLAR
    def konus(metin):
        global sayi

        sayi += 1

        tts = gTTS(text=metin, lang="tr", slow=False)
        dosya = "ses" + str(sayi) + ".mp3"
        tts.save(dosya)
        playsound.playsound(dosya)

    def kapat():
        x = "Elveda, senin için hep burada olacağım."
        print("Bernard: " + x)
        Komut.konus(x)
        sys.exit()

    def tablo_olustur():
        con = sqlite3.connect("hesap_bilgileri.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS HesapBilgileri (Platform TEXT, Eposta TEXT, Parola TEXT, Sehir TEXT)")
        con.commit()

    def kayit_ac():
        con = sqlite3.connect("kullanici_bilgileri.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS KullaniciBilgileri (Ad TEXT, Soyad TEXT, Hitap TEXT)")
        con.commit()

    def tabloya_ekle(platform, eposta, parola, sehir):
        con = sqlite3.connect("hesap_bilgileri.db")
        cursor = con.cursor() 
        cursor.execute("INSERT INTO HesapBilgileri VALUES(?,?,?,?)",(platform, eposta, parola, sehir))
        con.commit()

    def kayita_ekle(Ad, Soyad, Hitap):
        con = sqlite3.connect("kullanici_bilgileri.db")
        cursor = con.cursor() 
        cursor.execute("INSERT INTO KullaniciBilgileri VALUES(?,?,?)",(Ad, Soyad, Hitap))
        con.commit()

    def bilgi_ver():

        x = "Merhaba, hoş geldin! Beni en yüksek verimlilikte kullanabilmek için istenilen bilgileri doldurmalısın. Komutlarımın çalışabilmesi adına doldurduğun bilgilerin tamamı doğru olmalıdır. Hesabın olmayan platformlar için istenilen bilgilere 'Boş' yazabilirsin."
        print("Bernard: " + x)
        Komut.konus(x)

        time.sleep(1)

        x = "Netflix hesabına giriş yapmak için gerekli olan bilgileri gir."
        print("Bernard: " + x)
        Komut.konus(x)

        time.sleep(1)

        netflix_platform = "Netflix"
        netflix_eposta = input("Netflix e-posta: ")
        netflix_parola = input("Netflix parola: ")
        netflix_sehir = "Boş"

        Komut.tabloya_ekle(netflix_platform, netflix_eposta, netflix_parola, netflix_sehir)

        time.sleep(1)

        x = "Spotify hesabına giriş yapmak için gerekli olan bilgileri gir."
        print("Bernard: " + x)
        Komut.konus(x)

        time.sleep(1)

        spotif_platform = "Spotify"
        spotify_eposta = input("Spotify e-posta: ")
        spotify_parola = input("Spotify parola: ")
        spotif_sehir = "Boş"

        Komut.tabloya_ekle(spotif_platform, spotify_eposta, spotify_parola, spotif_sehir)

        time.sleep(1)

        x = "Yemeksepeti hesabına giriş yapmak için gerekli olan bilgileri gir."
        print("Bernard: " + x)
        Komut.konus(x)

        time.sleep(1)

        yemeksepeti_platform = "Yemeksepeti"
        yemeksepeti_eposta = input("Yemeksepeti e-posta: ")
        yemeksepeti_parola = input("Yemeksepeti parola: ")
        yemeksepeti_sehir = input("Yemeksepeti hizmetinden yararlanacağınız şehir: ")

        Komut.tabloya_ekle(yemeksepeti_platform, yemeksepeti_eposta, yemeksepeti_parola, yemeksepeti_sehir)

        time.sleep(1)

        x = "Gmail hesabına giriş yapmak için gerekli olan bilgileri gir."
        print("Bernard: " + x)
        Komut.konus(x)

        time.sleep(1)

        gmail_platform = "Gmail"
        gmail_eposta = input("Gmail e-posta: ")
        gmail_parola = input("Gmail parola: ")
        gmail_sehir = "Boş"

        Komut.tabloya_ekle(gmail_platform, gmail_eposta, gmail_parola, gmail_sehir)

        time.sleep(1)

    def kayit_ol():
        i = 0
        c = 0 

        gerekli_platformlar = ["Netflix", "Spotify", "Yemeksepeti", "Gmail"]

        Komut.tablo_olustur()
        Komut.kayit_ac()

        with sqlite3.connect("hesap_bilgileri.db") as db:
            cursor = db.cursor()
            platformlar = [Platform[0] for Platform in cursor.execute("SELECT Platform from HesapBilgileri")]

            if (len(platformlar) == 0):    
                Komut.bilgi_ver()

            elif (0 < len(platformlar) < len(gerekli_platformlar)):
                while i < len(gerekli_platformlar):
                    try:
                        if (gerekli_platformlar[i] == platformlar[i]):
                            i += 1

                    except IndexError:

                        if c == 0:
                            x = "Merhaba, hoş geldin. Anlaşılan, bilgilerinde eksiklik var."
                            print("Bernard: " + x)
                            Komut.konus(x)

                            c += 1

                        if gerekli_platformlar[i] == "Spotify":

                            time.sleep(1)

                            x = "Spotify hesabına giriş yapmak için gerekli olan bilgileri gir."
                            print("Bernard: " + x)
                            Komut.konus(x)

                            time.sleep(1)

                            spotif_platform = "Spotify"
                            spotify_eposta = input("Spotify e-posta: ")
                            spotify_parola = input("Spotify parola: ")
                            spotif_sehir = "Boş"

                            Komut.tabloya_ekle(spotif_platform, spotify_eposta, spotify_parola, spotif_sehir)

                            time.sleep(1)

                            i += 1

                        elif gerekli_platformlar[i] == "Yemeksepeti":

                            time.sleep(1)

                            x = "Yemeksepeti hesabına giriş yapmak için gerekli olan bilgileri gir."
                            print("Bernard: " + x)
                            Komut.konus(x)


                            time.sleep(1)

                            yemeksepeti_platform = "Yemeksepeti"
                            yemeksepeti_eposta = input("Yemeksepeti e-posta: ")
                            yemeksepeti_parola = input("Yemeksepeti parola: ")
                            yemeksepeti_sehir = input("Yemeksepeti hizmetinden yararlanacağınız şehir: ")

                            Komut.tabloya_ekle(yemeksepeti_platform, yemeksepeti_eposta, yemeksepeti_parola, yemeksepeti_sehir)

                            time.sleep(1)

                            i += 1

                        elif gerekli_platformlar[i] == "Gmail":
                            time.sleep(1)

                            x = "Gmail hesabına giriş yapmak için gerekli olan bilgileri gir."
                            print("Bernard: " + x)
                            Komut.konus(x)

                            time.sleep(1)

                            gmail_platform = "Gmail"
                            gmail_eposta = input("Gmail e-posta: ")
                            gmail_parola = input("Gmail parola: ")
                            gmail_sehir = "Boş"

                            Komut.tabloya_ekle(gmail_platform, gmail_eposta, gmail_parola, gmail_sehir)

                            time.sleep(1)

                            i += 1

            else:
                pass

        Komut.kayit_ac()

        with sqlite3.connect("kullanici_bilgileri.db") as db: 
            cursor = db.cursor()
            cursor.execute("Select * From KullaniciBilgileri")
            bilgiler = cursor.fetchall()

            if len(bilgiler) == 0:

                if i == 0:
                    x = "Hoş geldin, ben Bernard. Seni daha iyi tanımak ve daha iyi bir hizmet sunmak için senden birkaç bilgi isteyeceğim."
                    print("Bernard: " + x)
                    Komut.konus(x)

                    i += 1

                time.sleep(1)

                x = "Adını söyleyebilir misin?"
                print("Bernard: " + x)
                Komut.konus(x)

                ad = input("Adın: ")

                time.sleep(1)

                x = "Soyadını söyleyebilir misin?"
                print("Bernard: " + x)
                Komut.konus(x)

                soyad = input("Soydın: ")

                time.sleep(1)

                x = "Sana nasıl hitap etmeliyim?"
                print("Bernard: " + x)
                Komut.konus(x)

                hitap = input("Hitap: ")

                if hitap == None:
                    hitap = "Kullanıcı"

                time.sleep(1)

                Komut.kayita_ekle(ad, soyad, hitap)

            else:
                kullanici_bilgileri = bilgiler[0]

                ad = kullanici_bilgileri[0]
                soyad = kullanici_bilgileri[1]
                hitap = kullanici_bilgileri[2]

                return ad, soyad, hitap 
  
    def tarih():

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Hangi günün tarihini öğrenmek istiyorsunuz?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)
        tarih = ""

        try:
            tarih = r.recognize_google(ses, language="tr-tr")
            print(hitap + ": " + tarih)

            time.sleep(1)

            print("Bernard: " + str(tarih_bul(tarih)))
            Komut.konus(str(tarih_bul(tarih)))

        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

    def netflix():

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Açmamı istediğin içeriğin adı ne?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            icerik = ""
            icerik = r.recognize_google(ses, language="tr-tr")
            icerik = icerik.title()
            print(hitap + ": " + icerik)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        con = sqlite3.connect("hesap_bilgileri.db")
        cursor = con.cursor()

        path = "C:\Program Files (x86)\chromedriver.exe"

        chrome_acik_kalsin = Options()
        chrome_acik_kalsin.add_experimental_option("detach", True)
        driver = webdriver.Chrome(path, chrome_options=chrome_acik_kalsin)

        cursor.execute("Select * From HesapBilgileri[0]")
        data = cursor.fetchall()
        netflix = data[0]

        netflix_eposta = netflix[1]
        netflix_parola = netflix[2]

        time.sleep(1)

        driver.get("https://www.netflix.com/tr/login")

        time.sleep(1)

        driver.maximize_window()

        time.sleep(1)

        eposta = driver.find_element_by_id("id_userLoginId")
        eposta.send_keys(netflix_eposta)

        time.sleep(1)

        parola = driver.find_element_by_id("id_password")
        parola.send_keys(netflix_parola)

        time.sleep(1)

        oturum_ac = driver.find_element_by_class_name("login-button")
        oturum_ac.click()

        time.sleep(5)

        profiller = driver.find_elements_by_class_name("profile-link")
        profil = profiller[0]
        profil.click()

        time.sleep(3)

        ara_buton = driver.find_element_by_class_name("searchTab")
        ara_buton.click()

        time.sleep(1)

        ara_bar = driver.find_element_by_name("searchInput")
        ara_bar.send_keys(icerik)
        
        time.sleep(3)

        ac = driver.find_element_by_class_name("slider-item-0")
        ac.click()

        time.sleep(5)

        try:
            oynat = driver.find_element_by_xpath("//*[@id='pane-Overview']/div/div/div/div[1]/div/div[4]/a[2]/button")
            oynat.click()

        except NoSuchElementException:
            oynat = driver.find_element_by_xpath("//*[@id='pane-Overview']/div/div/div/div[1]/div/div[5]/a[2]/button")
            oynat.click()

        time.sleep(3)

        actions = ActionChains(driver)
        actions.send_keys('F')
        actions.perform()

    def spotify():
        con = sqlite3.connect("hesap_bilgileri.db")
        cursor = con.cursor()

        path = "C:\Program Files (x86)\chromedriver.exe"

        chrome_acik_kalsin = Options()
        chrome_acik_kalsin.add_experimental_option("detach", True)
        driver = webdriver.Chrome(path, chrome_options=chrome_acik_kalsin)

        cursor.execute("Select * From HesapBilgileri[0]")
        data = cursor.fetchall()
        spotify = data[1]

        spotify_eposta = spotify[1]
        spotify_parola = spotify[2]

        driver.get("https://accounts.spotify.com/tr/login")

        time.sleep(1)

        driver.maximize_window()

        time.sleep(1)

        eposta = driver.find_element_by_id("login-username")
        parola = driver.find_element_by_id("login-password")

        eposta.send_keys(spotify_eposta)

        time.sleep(1)

        parola.send_keys(spotify_parola)

        time.sleep(1)
        
        oturum_ac = driver.find_element_by_id("login-button")
        oturum_ac.click()

        time.sleep(1)

        devam = driver.find_elements_by_xpath("//*[@id='app']/body/div/div[2]/div/div/div[4]/div/a")

        if len(devam) == 0:
            time.sleep(5)

            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()

        else:
            devam[0].click()

            time.sleep(5)
            actions = ActionChains(driver)
            actions.send_keys(Keys.SPACE)
            actions.perform()

    def yemeksepeti():
        def parcaBul(parca):
            def sepetOlustur():

                bekle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, parca)))

                try:                        
                    bekle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cboxLoadedContent")))

                    time.sleep(3)
                                
                    secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                    time.sleep(3)

                    for secenek in secenekler:

                        sec = Select(secenek)
                        sec.select_by_index(1)

                    time.sleep(3)

                    secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                    time.sleep(3)

                    for secenek in secenekler:

                        sec = Select(secenek)
                        sec.select_by_index(1)

                    time.sleep(3)

                except ElementNotInteractableException:

                    time.sleep(5)

                    araEkran = driver.find_element_by_xpath("//*[@id='cboxLoadedContent']/div/div[1]/div/div/div[2]")
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", araEkran)

                    time.sleep(3)

                    secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                    time.sleep(3)

                    for secenek in secenekler:

                        sec = Select(secenek)
                        sec.select_by_index(1)

                    time.sleep(3)

                    secenekler = list(driver.find_elements_by_class_name("optionSelect"))

                    time.sleep(3)

                    for secenek in secenekler:

                        sec = Select(secenek)
                        sec.select_by_index(1)

                    time.sleep(3)

                finally:

                    time.sleep(3)

                    sepeteEkle = driver.find_element_by_xpath("//*[@id='cboxLoadedContent']/div/div[2]/div/div[2]/button")
                    sepeteEkle.click()

                    time.sleep(3)

                    driver.execute_script("window.scroll(0, 0);")

                    time.sleep(3)

            if (parca.upper() == "YOK"):
                pass

            else:
                parcaSecimi = driver.find_element_by_link_text(parca)
                parcaSecimi.click()
                try:
                    sepetOlustur()

                except StaleElementReferenceException:

                    time.sleep(5)
                                
                    bekle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, parca)))

                    time.sleep(3)

                    parcaSecimi = driver.find_element_by_link_text(parca)
                    parcaSecimi.click()

                    time.sleep(3)

                    sepetOlustur()

                except ElementClickInterceptedException:

                    time.sleep(5)

                    sepetOlustur()

                except TimeoutError:

                    time.sleep(5)

                    sepetOlustur()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Hangi restorandan sipariş vereceksin?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            restoran = ""
            restoran = r.recognize_google(ses, language="tr-tr")
            restoran = restoran.title()
            print(hitap + ": " + restoran)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Sipariş vereceğin ilk parçayı söyler misin?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            birinci_parca = ""
            birinci_parca = r.recognize_google(ses, language="tr-tr")
            birinci_parca = birinci_parca.title()
            print(hitap + ": " + birinci_parca)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Sipariş edeceğin ikinci parçayı söyler misin? İstemiyorsan 'Yok' demelisin."
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            ikinci_parca = ""
            ikinci_parca = r.recognize_google(ses, language="tr-tr")
            ikinci_parca = ikinci_parca.title()
            print(hitap + ": " + ikinci_parca)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Sipariş edeceğin üçüncü parçayı söyler misin? İstemiyorsan 'Yok' demelisin."
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            ucuncu_parca = ""
            ucuncu_parca = r.recognize_google(ses, language="tr-tr")
            ucuncu_parca = ucuncu_parca.title()
            print(hitap + ": " + ucuncu_parca)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        con = sqlite3.connect("hesap_bilgileri.db")
        cursor = con.cursor()

        path = "C:\Program Files (x86)\chromedriver.exe"

        chrome_acik_kalsin = Options()
        chrome_acik_kalsin.add_experimental_option("detach", True)
        driver = webdriver.Chrome(path, chrome_options=chrome_acik_kalsin)

        cursor.execute("Select * From HesapBilgileri[0]")
        data = cursor.fetchall()
        yemeksepeti = data[2]

        yemeksepeti_eposta = yemeksepeti[1]
        yemeksepeti_parola = yemeksepeti[2]
        sehir = yemeksepeti[3]
        sehir = sehir.lower()
        sehir = sehir.replace("ş", "s")
        sehir = sehir.replace("ç", "c")
        sehir = sehir.replace("ö", "o")
        sehir = sehir.replace("ğ", "g")
        sehir = sehir.replace("ü", "u")
        sehir = sehir.replace("ı", "i")


        driver.get("https://www.yemeksepeti.com/"+sehir)

        time.sleep(1)

        driver.maximize_window()

        time.sleep(1)

        username = driver.find_element_by_id("UserName")
        username.send_keys(yemeksepeti_eposta)

        time.sleep(1)

        password = driver.find_element_by_id("password")
        password.send_keys(yemeksepeti_parola)

        time.sleep(1)

        giris = driver.find_element_by_id("ys-fastlogin-button")
        giris.click()

        time.sleep(3)

        evButonu = driver.find_element_by_class_name("address-labels")
        evButonu.click()

        time.sleep(3)

        ara = driver.find_element_by_class_name("search-box")
        ara.send_keys(restoran)

        time.sleep(1)

        ara.send_keys(Keys.ENTER)

        time.sleep(6)

        restoranaGiris = driver.find_element_by_class_name("restaurantName")
        restoranaGiris.click()

        time.sleep(3)

        parcaBul(birinci_parca)
        parcaBul(ikinci_parca)
        parcaBul(ucuncu_parca)

        time.sleep(5)

        sepetOnay = driver.find_element_by_class_name("confirm-basket")
        sepetOnay.click()

        time.sleep(10)

        kapida_nakit = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[9]/div/div/div/div/div[2]/div/div[1]/label/input")
        kapida_nakit.click()

        x = "İstediğiniz parçalar sepete eklendi."
        print("Bernard: " + x)
        Komut.konus(x)

    def gmail():
        
        con = sqlite3.connect("hesap_bilgileri.db")
        cursor = con.cursor()

        cursor.execute("Select * From HesapBilgileri[0]")
        data = cursor.fetchall()
        gmail = data[3]

        gmail_eposta = gmail[1]
        gmail_parola = gmail[2]

        sor = "Postayı alacak adresi girebilir misin?"
        print("Bernard: " + sor)
        Komut.konus(sor)

        alici = input("Alıcı: ")

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Postanın başlığı ne olacak?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            baslik = ""
            baslik = r.recognize_google(ses, language="tr-tr")
            baslik = baslik.title()
            print(hitap + ": " + baslik)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Postanın içeriği ne olacak?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            posta = ""
            posta = r.recognize_google(ses, language="tr-tr")
            print(hitap + ": " + posta)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        try:
            mesaj = MIMEMultipart()
            mesaj["From"] = gmail_eposta
            mesaj["To"] = alici
            mesaj["Subject"] = baslik

            mesaj.attach(MIMEText(posta, "plain"))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(gmail_eposta, gmail_parola)
            yazi = mesaj.as_string()

            x = "Posta gönderiliyor."
            print("Bernard: " + x)
            Komut.konus(x)

            server.sendmail(gmail_eposta, alici, yazi)

            x = "Posta gönderildi."
            print("Bernard: " + x)
            Komut.konus(x)

        except SMTPAuthenticationError:
            x = "Lütfen Gmail hesabında 'Daha az güvenli uygulamalara' izin ver."
            print("Bernard: " + x)
            Komut.konus(x)

            x = "İşte bu değişikliği yapabilmek için link: "
            print("Bernard: " + x)
            Komut.konus(x)
            print("https://myaccount.google.com/lesssecureapps")

    def youtube():
        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Açmamı istediğin videonun adı ne?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            video = ""
            video = r.recognize_google(ses, language="tr-tr")
            video = video.title()
            print(hitap + ": " + video)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        path = "C:\Program Files (x86)\chromedriver.exe"

        chrome_acik_kalsin = Options()
        chrome_acik_kalsin.add_experimental_option("detach", True)
        driver = webdriver.Chrome(path, chrome_options=chrome_acik_kalsin)

        time.sleep(1)

        driver.get("https://www.youtube.com")

        time.sleep(1)

        driver.maximize_window()

        time.sleep(3)

        arama_barı = driver.find_element_by_xpath("//input[@id='search']")
        arama_barı.send_keys(video)
        arama_barı.send_keys(Keys.ENTER)

        time.sleep(3)

        kanal = driver.find_elements_by_class_name("channel-link")

        if len(kanal) == 0:
            time.sleep(3)

            wait = WebDriverWait(driver, 3)
            visible = EC.visibility_of_element_located

            driver.get('https://www.youtube.com/results?search_query={}'.format(str(video)))

            wait.until(visible((By.ID, "video-title")))
            driver.find_element_by_id("video-title").click()

            time.sleep(1)

            acilan_video_adi = str(driver.find_element_by_xpath("//*[@id='container']/h1/yt-formatted-string").text)

            try:
                time.sleep(1)
                reklam = driver.find_elements_by_class_name("video-ads")

            except NoSuchElementException:
                pass
                
            if len(reklam) != 0:
                try:
                    reklami_gec = driver.find_element_by_class_name("ytp-ad-skip-button")

                    time.sleep(5)
                    
                    reklami_gec.click()

                    time.sleep(1)

                    oynayan_video = driver.find_element_by_xpath("//*[@id='movie_player']")
                    oynayan_video.send_keys(Keys.SPACE)

                    print("Açılan video: " + acilan_video_adi)
                    Komut.konus("Açılan video: " + acilan_video_adi)

                    oynayan_video.send_keys(Keys.SPACE)

                except NoSuchElementException:

                    time.sleep(1)

                    oynayan_video = driver.find_element_by_xpath("//*[@id='movie_player']")
                    oynayan_video.send_keys(Keys.SPACE)

                    print("Açılan video: " + acilan_video_adi)
                    Komut.konus("Açılan video: " + acilan_video_adi)

                    oynayan_video.send_keys(Keys.SPACE)
        
            else:

                time.sleep(1)

                oynayan_video = driver.find_element_by_xpath("//*[@id='movie_player']")
                oynayan_video.send_keys(Keys.SPACE)

                print("Açılan video: " + acilan_video_adi)
                Komut.konus("Açılan video: " + acilan_video_adi)

                oynayan_video.send_keys(Keys.SPACE)
        
        else:
            time.sleep(3)

            acilacak_kanal = kanal[0]

            acilan_kanal_adi = str(driver.find_element_by_xpath("//*[@id='channel-title']").text)

            acilacak_kanal.click()

            time.sleep(3)

            try:
                time.sleep(2)

                anladim = driver.find_element_by_xpath("//*[@id='accept-button']/yt-button-renderer/a")
                anladim.click()

                time.sleep(2)

            except:
                pass

            videolar = driver.find_element_by_xpath("//*[@id='tabsContent']/paper-tab[2]")
            videolar.click()

            time.sleep(1)

            x = "Açmamı istediğin video ile yapılan aramada çıkan ilk sonuç bir kanal olduğu için o kanalın videolar sekmesini açtım."
            print("Bernard: " + x)
            Komut.konus(x)

            time.sleep(1)

            y = "Açılan kanal: " + acilan_kanal_adi

            print(y)
            Komut.konus(y)

    def google():
        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Google'da aratmak istediğin şey ne?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            aratma = ""
            aratma = r.recognize_google(ses, language="tr-tr")
            aratma = aratma.title()
            print(hitap + ": " + aratma)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        path = "C:\Program Files (x86)\chromedriver.exe"

        chrome_acik_kalsin = Options()
        chrome_acik_kalsin.add_experimental_option("detach", True)
        driver = webdriver.Chrome(path, chrome_options=chrome_acik_kalsin)

        time.sleep(1)

        driver.get("https://www.google.com")

        time.sleep(1)

        driver.maximize_window()

        time.sleep(1)

        arama_bari = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        arama_bari.send_keys(aratma)
        arama_bari.send_keys(Keys.ENTER)

        time.sleep(1)

        try:
            biyografi = driver.find_element_by_xpath("//*[@id='kp-wp-tab-overview']/div[1]/div/div/div/div[1]/div/div/div/div").text.replace("Vikipedi", "")
            biyografi = biyografi.replace("Açıklama", "")
            driver.quit()

            if biyografi == "Tümünü görüntüle":
                cevap = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div[1]/div/div[2]").text
                driver.quit()

                print("Bernard: " + cevap)
                Komut.konus(cevap)

            else:
                pass

            print("Bernard: " + biyografi)
            Komut.konus(biyografi)

        except:
            try:
                cevap = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div[1]/div/div[2]").text
                driver.quit()

                if cevap == "Tümünü görüntüle":
                    cevap = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div[1]/div/div[2]/div").text
                    driver.quit()

                    print("Bernard: " + cevap)
                    Komut.konus(cevap)

                else:
                    pass

                print("Bernard: " + cevap)
                Komut.konus(cevap)

            except:
                try:
                    cevap = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div[1]/div/div[2]").text
                    driver.quit()

                    print("Bernard: " + cevap)
                    Komut.konus(cevap)

                except:
                    try:
                        link_basligi = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/a/h3")
                        link_basligi.click()

                        time.sleep(1)

                        link = driver.current_url
                        driver.quit()

                        print("Bernard: İşte aradığın cevap burada: " + link)
                        Komut.konus("İşte aradığın cevap burada")

                    except:
                        try:
                            wait = WebDriverWait(driver, 3)
                            visible = EC.visibility_of_element_located

                            driver.get('https://www.youtube.com/results?search_query={}'.format(str(aratma)))

                            wait.until(visible((By.ID, "video-title")))
                            driver.find_element_by_id("video-title").click()

                            time.sleep(3)

                            acilan_video_adi = str(driver.find_element_by_xpath("//*[@id='container']/h1/yt-formatted-string").text)

                            x = "Arama sonucu çıkan ilk şey bir video olduğu için videoyu açtım. Açılan video: " + acilan_video_adi
                            print("Bernard: " + x)
                            Komut.konus(x)

                        except:
                            x = "Yapmak istediğin arama bir hataya neden oldu."
                            print("Bernard: " + x)
                            Komut.konus(x)

    def vikipedi():
        aratma = None
        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Vikipedi'de ne aratmak istersin?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            aratma = ""
            aratma = r.recognize_google(ses, language="tr-tr")
            aratma = aratma.title()
            print(hitap + ": " + aratma)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        sonuc_sayisi = len(wikipedia.search(aratma))
        x = "Bernard: " + str(sonuc_sayisi) + " tane sonuç bulundu. Bunlardan ilki getiriliyor."
        y = str(sonuc_sayisi) + " tane sonuç bulundu. Bunlardan ilki getiriliyor."
        print(x)
        Komut.konus(y)

        ozet = wikipedia.summary(aratma, sentences = 3)
        x = aratma + " için özet:\n"
        y = aratma + " için özet:\n" + ozet
        print(y)
        Komut.konus(x)

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Daha detaylı bilgi ister misiniz?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            cevap = ""
            cevap = r.recognize_google(ses, language="tr-tr")
            cevap = cevap
            print(hitap + ": " + cevap)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        if cevap.upper() == "EVET":
            bilgi = wikipedia.page(aratma).content
            xbilgi = aratma + " için detaylı bilgi:\n"
            ybilgi = aratma + " için detaylı bilgi:\n" + bilgi
            Komut.konus(xbilgi)
            print(ybilgi)

        else:
            pass
    
    def whatsapp():
        path = "C:\Program Files (x86)\chromedriver.exe"

        driver = webdriver.Chrome(path)
        driver.get("https://web.whatsapp.com")

        time.sleep(1)

        x = "Lütfen 10 saniye içerisinde QR kodu tarat."
        print("Bernard: " + x)
        Komut.konus(x)

        time.sleep(10)

        konusmalar = driver.find_elements_by_class_name("_210SC")
        konusmalar_isimler = driver.find_elements_by_class_name("_357i8")
        konusmalar_isimler_yazilar = []

        for i in konusmalar_isimler:
            i = i.text
            konusmalar_isimler_yazilar.append(i)

        if len(konusmalar) == 0:
            x = "Lütfen daha sonra tekrar dene ve QR kodu taratmayı unutma."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        else:
            x = "Taratma başarılı."
            print("Bernard: " + x)
            Komut.konus(x)

            with sr.Microphone() as source:
                time.sleep(1)
                sor = "Kime mesaj atmak istiyorsun?"
                print("Bernard: " + sor)
                Komut.konus(sor)
                ses = r.listen(source)

            try:
                kisi = ""
                kisi = r.recognize_google(ses, language="tr-tr")
                print(hitap + ": " + kisi)
                
            except sr.UnknownValueError:
                x = "Özür dilerim. Ne dediğini anlayamadım."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

            if kisi in konusmalar_isimler_yazilar:
                x = kisi + " kişisi bulundu."
                print("Bernard: " + x)
                Komut.konus(x)

                siralama = konusmalar_isimler_yazilar.index(kisi)
                konusmalar_isimler[siralama].click()

                time.sleep(3)

                with sr.Microphone() as source:
                    time.sleep(1)
                    sor = kisi + " kişisine ne iletmek istiyorsun?"
                    print("Bernard: " + sor)
                    Komut.konus(sor)
                    ses = r.listen(source)

                try:
                    ileti = ""
                    ileti = r.recognize_google(ses, language="tr-tr")
                    print(hitap + ": " + ileti)
                    
                except sr.UnknownValueError:
                    x = "Özür dilerim. Ne dediğini anlayamadım."
                    print("Bernard: " + x)
                    Komut.konus(x)
                    sys.exit()

                time.sleep(2)

                girdi = driver.find_element_by_class_name("_3uMse")

                time.sleep(2)

                girdi.send_keys(ileti)

                time.sleep(2)

                girdi.send_keys(Keys.ENTER)

                time.sleep(1)

                x = kisi + " kişisine " + ileti + " mesajı gönderildi."
                print("Bernard: " + x)
                Komut.konus(x)

            else:
                x = kisi + " kişisi bulunamadı."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

    def ceviri():

        with sr.Microphone() as source:
            time.sleep(1)
            x = "Hangi dile çeviri yapmak istiyorsun? Şu anlık İngilizce'ye, Almanca'ya ve İspanyolca'ya kelime çevirisi yapabilirim."
            print("Bernard: " + x)
            Komut.konus(x)
            ses = r.listen(source)

        try:
            dil = ""
            dil = r.recognize_google(ses, language="tr-tr")
            dil = dil.capitalize()
            print(hitap + ": " + dil)
            
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadım."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        if dil == "İngilizce":

            with sr.Microphone() as source:
                time.sleep(1)
                x = "Çevirmek istediğin sözcüğü söyler misin?"
                print("Bernard: " + x)
                Komut.konus(x)
                ses = r.listen(source)

            try:
                sozcuk = ""
                sozcuk = r.recognize_google(ses, language="tr-tr")
                sozcuk = sozcuk.capitalize()
                print(hitap + ": " + sozcuk)
                
            except sr.UnknownValueError:
                x = "Özür dilerim. Ne dediğini anlayamadım."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

            path = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get("https://tureng.com/tr/turkce-ingilizce")

            time.sleep(1)

            arama_bari = driver.find_element_by_xpath("//*[@id='searchTerm']")
            arama_bari.send_keys(sozcuk)
            arama_bari.send_keys(Keys.ENTER)

            time.sleep(1)

            try:
                sonuc = driver.find_element_by_xpath("//*[@id='englishResultsTable']/tbody/tr[4]/td[4]/a").text
                driver.quit()
                sozcuk = sozcuk.lower()
                
                time.sleep(1)

            except:
                driver.quit()
                x = "Üzgünüm, aradığın kelimeyi bulamadım."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

            sonuc = sonuc.split()

            if len(sonuc) > 1:
                sonucx = " ".join(sonuc)
                x = "Aradığın " + "'" + sozcuk + "'" + " sözcüğünün İngilizce karşılığı " + "'" + sonucx + "' kalıbı."
                print("Bernard: " + x)
                Komut.konus(x)

            else:
                sonuc = sonuc[0]
                x = "Aradığın " + "'" + sozcuk + "'" + " sözcüğünün İngilizce karşılığı " + "'" + sonuc + "' sözcüğü."
                print("Bernard: " + x)
                Komut.konus(x)

        elif dil == "Almanca":
            with sr.Microphone() as source:
                time.sleep(1)
                x = "Çevirmek istediğin sözcüğü söyler misin?"
                print("Bernard: " + x)
                Komut.konus(x)
                ses = r.listen(source)

            try:
                sozcuk = ""
                sozcuk = r.recognize_google(ses, language="tr-tr")
                sozcuk = sozcuk.capitalize()
                print(hitap + ": " + sozcuk)
                
            except sr.UnknownValueError:
                x = "Özür dilerim. Ne dediğini anlayamadım."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

            path = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get("https://tr.bab.la/sozluk/turkce-almanca")

            time.sleep(1)

            arama_bari = driver.find_element_by_xpath("//*[@id='bablasearch']")
            arama_bari.send_keys(sozcuk)
            arama_bari.send_keys(Keys.ENTER)

            time.sleep(1)

            try:
                sonuc = driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/ul/li[1]/a").text
                driver.quit()
                sozcuk = sozcuk.lower()
                
                time.sleep(1)

            except: 
                driver.quit()
                x = "Üzgünüm, aradığın kelimeyi bulamadım."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

            sonuc = sonuc.split()

            if len(sonuc) > 1:
                sonucx = " ".join(sonuc)
                x = "Aradığın " + "'" + sozcuk + "'" + " sözcüğünün Almanca karşılığı " + "'" + sonucx + "' kalıbı."
                print("Bernard: " + x)
                Komut.konus(x)

            else:
                sonuc = sonuc[0]
                x = "Aradığın " + "'" + sozcuk + "'" + " sözcüğünün Almanca karşılığı " + "'" + sonuc + "' sözcüğü."
                print("Bernard: " + x)
                Komut.konus(x)

        elif dil == "İspanyolca":
            with sr.Microphone() as source:
                time.sleep(1)
                x = "Çevirmek istediğin sözcüğü söyler misin?"
                print("Bernard: " + x)
                Komut.konus(x)
                ses = r.listen(source)

            try:
                sozcuk = ""
                sozcuk = r.recognize_google(ses, language="tr-tr")
                sozcuk = sozcuk.capitalize()
                print(hitap + ": " + sozcuk)
                
            except sr.UnknownValueError:
                x = "Özür dilerim. Ne dediğini anlayamadım."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

            path = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get("https://www.dict.com/ispanyolca-turkce")

            time.sleep(1)

            arama_bari = driver.find_element_by_xpath("//*[@id='word']")
            arama_bari.send_keys(sozcuk)
            arama_bari.send_keys(Keys.ENTER)

            time.sleep(1)

            try:
                sonuc = driver.find_element_by_xpath("//*[@id='entry-wrapper']/table/tbody/tr[2]/td[2]/span[1]/w").text
                driver.quit()
                sozcuk = sozcuk.lower()
                
                time.sleep(1)

            except: 
                driver.quit()
                x = "Üzgünüm, aradığın kelimeyi bulamadım."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

            sonuc = sonuc.split()

            if len(sonuc) > 1:
                sonucx = " ".join(sonuc)
                x = "Aradığın " + "'" + sozcuk + "'" + " sözcüğünün İspanyolca karşılığı " + "'" + sonucx + "' kalıbı."
                print("Bernard: " + x)
                Komut.konus(x)

            else:
                sonuc = sonuc[0]
                x = "Aradığın " + "'" + sozcuk + "'" + " sözcüğünün İspanyolca karşılığı " + "'" + sonuc + "' sözcüğü."
                print("Bernard: " + x)
                Komut.konus(x)

        else:
            x = "Lütfen İngilizce, Almanca ve İspanyolca dillerinden birini seç."
            print("Bernard: " + x)
            Komut.konus(x)

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

        gun_sayisi = None

        with sr.Microphone() as source:
            ses = r.listen(source)

        try:
            i = 0
            gun_sayisi = r.recognize_google(ses, language="tr-tr")

            print(hitap + ": " + gun_sayisi)

            if str(gun_sayisi):
                birler = ["bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]

                while i < len(birler):
                    if gun_sayisi == birler[i]:
                        gun_sayisi = i + 1
                        gun_sayisi = int(gun_sayisi)

                    else:
                        i += 1
            else:
                gun_sayisi = int(gun_sayisi)

        except sr.UnknownValueError:
            x = "Ne dediğini anlayamadım. Lütfen komutu tekrar çağır."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

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
            baslangic = baslangic.replace("TS", "")
            baslangic = baslangic.replace("T", " ")
            baslangic = baslangic.replace("+", "")
            baslangic = baslangic.replace("03:00", "")
            print("Bernard: " + baslangic + " " + etkinlik["summary"])
            Komut.konus(baslangic + " . " + etkinlik["summary"])
    
    def google_auth():

        global calendar_id
        global service

        scopes = ['https://www.googleapis.com/auth/calendar']
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
        credentials = flow.run_console()
        pickle.dump(credentials, open("token.pkl", "wb"))
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result['items'][0]['id']

        return calendar_id, service

    def etkinlik_ekle():

        zaman_dilimi = "Europe/Istanbul"

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Hangi güne etkinlik eklemek istiyorsunuz?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        tarih = ""
        
        try:
            tarih = r.recognize_google(ses, language="tr-tr")
            if "sonra" in tarih:
                tarih = tarih_bul(tarih)
                print(hitap + ": " + str(tarih))

            elif "sonra" not in tarih:
                tarih = tarih_bul(tarih)
                print(hitap + ": " + str(tarih))

            time.sleep(1)

        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Etkinlik saat kaçta başlayacak?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        baslangic = ""

        try:
            baslangic = r.recognize_google(ses, language="tr-tr")

            for harf in "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç:.,;":
                baslangic = baslangic.replace(harf, "")
                baslangic = baslangic.replace(" ", "")

            baslangic_saat = baslangic[:2]
            baslangic_dakika = baslangic[2:]

            baslangic = baslangic_saat + ":" + baslangic_dakika
            baslangic = baslangic + ":00"

            print(hitap + ": " + baslangic)

            time.sleep(1)
        
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Etkinlik saat kaçta bitecek?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        bitis = ""

        try:
            bitis = r.recognize_google(ses, language="tr-tr")

            for harf in "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç:.,;'":
                bitis = bitis.replace(harf, "")
                bitis = bitis.replace(" ", "")

            bitis_saat = bitis[:2]
            bitis_dakika = bitis[2:]

            bitis = bitis_saat + ":" + bitis_dakika
            bitis = bitis + ":00"

            print(hitap + ": " + bitis)

            time.sleep(1)
        
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Etkinliğin adı ne?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        ad = ""

        try:
            ad = r.recognize_google(ses, language="tr-tr")
            ad = ad.title()
            print(hitap + ": " + ad)

            time.sleep(1)
        
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Etkinlik nerede olacak?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        yer = ""

        try:
            yer = r.recognize_google(ses, language="tr-tr")
            yer = yer.title()
            print(hitap + ": " + yer)

            time.sleep(1)
        
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()
     
        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Etkinliğin açıklaması ne?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        aciklama = ""

        try:
            aciklama = r.recognize_google(ses, language="tr-tr")
            print(hitap + ": " + aciklama)

            time.sleep(1)
        
        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        baslangic_zamani_listesi = []
        bitis_zamani_listesi = []

        for i in str(tarih).split("-"):
            baslangic_zamani_listesi.append(i)
            bitis_zamani_listesi.append(i)

        for i in baslangic.split(":"):
            baslangic_zamani_listesi.append(i)

        for i in bitis.split(":"):
            bitis_zamani_listesi.append(i)

        bas_yil = int(baslangic_zamani_listesi[0])
        bas_ay = int(baslangic_zamani_listesi[1])
        bas_gun = int(baslangic_zamani_listesi[2])
        bas_saat = int(baslangic_zamani_listesi[3])
        bas_dak = int(baslangic_zamani_listesi[4])
        bas_san = int(baslangic_zamani_listesi[5])

        bit_yil = int(bitis_zamani_listesi[0])
        bit_ay = int(bitis_zamani_listesi[1])
        bit_gun = int(bitis_zamani_listesi[2])
        bit_saat = int(bitis_zamani_listesi[3])
        bit_dak = int(bitis_zamani_listesi[4])
        bit_san = int(bitis_zamani_listesi[5])

        baslangic_zamani = datetime.datetime(bas_yil, bas_ay, bas_gun, bas_saat, bas_dak, bas_san)
        bitis_zamani = datetime.datetime(bit_yil, bit_ay, bit_gun, bit_saat, bit_dak, bit_san)

        event = {
            'summary': ad,
            'location': yer,
            'description': aciklama,
            'start': {
                'dateTime': baslangic_zamani.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': zaman_dilimi,
            },
            'end': {
                'dateTime': bitis_zamani.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': zaman_dilimi,
            }
        }

        service.events().insert(calendarId=calendar_id, body=event).execute()

        x = "Girdiğiniz bilgiler doğrultusunda Google Takvim etkinliği oluşturuldu."
        print("Bernard: " + x)
        Komut.konus(x)

    def doviz_cevir():

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Çevirilecek birimi söyler misin?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            girdi_birim = ""
            girdi_birim = r.recognize_google(ses, language="tr-tr")
            girdi_birim = girdi_birim.upper()

            currency_dict = {
                "DOLAR": "USD",
                "AMERİKAN DOLARI".replace("İ", "I"): "USD",
                "EURO": "EUR",
                "STERLİN".replace("İ", "I"): "GBP", 
                "POUND": "GBP",
                "İNGİLİZ STERLİNİ".replace("İ", "I"): "GBP",
                "İNGİLİZ POUNDU".replace("İ", "I"): "GBP",
                "İSVİÇRE FRANGI".replace("İ", "I"): "CHF",
                "FRANK": "CHF",
                "KANADA DOLARI": "CAD",
                "RUBLE": "RUB",
                "RUS RUBLESİ".replace("İ", "I"): "RUB",
                "BİRLEŞİK ARAP EMİRLİKLERİ DİRHEMİ".replace("İ", "I"): "AED",
                "DİRHEM".replace("İ", "I"): "AED",
                "AVUSTRALYA DOLARI": "AUD",
                "DANİMARKA KRONU".replace("İ", "I"): "DKK",
                "KRON": "DKK",
                "İSVEÇ KRONU".replace("İ", "I"): "SEK",
                "NORVEÇ KRONU": "NOK",
                "JAPON YENİ".replace("İ", "I"): "JPY",
                "YEN": "JPY",
                "KUVEYT DİNARI".replace("İ", "I"): "KWD",
                "DİNAR".replace("İ", "I"): "KWD",
                "GÜNEY AFRİKA RANDI".replace("İ", "I"): "ZAR",
                "BAHREYN DİNARI".replace("İ", "I"):"BHD",
                "LİBYA DİNARI".replace("İ", "I"): "LYD",
                "SUUDİ ARABİSTAN RİYALİ".replace("İ", "I"): "SAR",
                "RİYAL".replace("İ", "I"): "SAR",
                "IRAK DİNARI".replace("İ", "I"): "IQD",
                "İSRAİL ŞEKELİ".replace("İ", "I"): "ILS",
                "İRAN RİYALİ".replace("İ", "I"): "IRR",
                "HİNDİSTAN RUPİSİ".replace("İ", "I"): "INR",
                "RUPİ".replace("İ", "I"): "INR",
                "MEKSİKA PESOSU".replace("İ", "I"): "MXN",
                "PESO": "MXN",
                "MACAR FORİNTİ".replace("İ", "I"): "HUF",
                "YENİ ZELANDA DOLARI".replace("İ", "I"): "NZD",
                "BREZİLYA REALİ".replace("İ", "I"): "BRL",
                "ENDONEZYA RUPİAHİ".replace("İ", "I"): "IDR",
                "ÇEK KORUNASI": "CSK",
                "POLONYA ZLOTİSİ".replace("İ", "I"): "PLN",
                "ZLOTİ".replace("İ", "I"): "PLN",
                "ZLOTY": "PLN",
                "ROMANYA LEYİ".replace("İ", "I"): "RON",
                "ÇİN YUANI".replace("İ", "I"): "CNY",
                "ARJANTİN PESOSU".replace("İ", "I"): "ARS",
                "ARNATUVLUK LEKİ".replace("İ", "I"): "ALL",
                "AZERBAYCAN MANATI": "AZN",
                "MANAT": "AZN",
                "BOSNA HERSEK MARKI".replace("İ", "I"): "BAM",
                "ŞİLİ PESOSU".replace("İ", "I"): "CLP",
                "KOLOMBİYA PESOSU".replace("İ", "I"): "COP",
                "KOSTA RİKA KOLONU".replace("İ", "I"): "CRC",
                "HONG KONG DOLARI": "HKD",
                "CEZAYİR DİNARI".replace("İ", "I"): "DZD",
                "MISIR LİRASI".replace("İ", "I"): "EGP",
                "ÜRDÜN DİNARI".replace("İ", "I"): "JOD",
                "HIRVAT KUNASI": "HRK",
                "İZLANDA KRONASI".replace("İ", "I"): "ISK",
                "GÜNEY KORE WONU": "KRW",
                "KAZAK TENGESİ".replace("İ", "I"): "KZT",
                "LÜBNAN LİRASI".replace("İ", "I"): "LBP",
                "SRİ LANKA RUPİSİ".replace("İ", "I"): "LKR",
                "FAS DİRHEMİ".replace("İ", "I"): "MAD",
                "MOLDOVYA LEUSU".replace("İ", "I"): "MDL",
                "MAKEDON DİNARI".replace("İ", "I"): "MKD",
                "MALEZYA RİNGGİTİ".replace("İ", "I"): "MYR",
                "UMMAN RİYALİ".replace("İ", "I"): "OMR",
                "PERU İNTİ".replace("İ", "I"): "PEN",
                "FİLİPİNLER PESOSU".replace("İ", "I"): "PHP",
                "PAKİSTAN RUPİSİ".replace("İ", "I"): "PKR",
                "KATAR RİYALİ".replace("İ", "I"): "QAR",
                "SIRBİSTAN DİNARI".replace("İ", "I"): "RSD",
                "SİNGAPUR DOLARI".replace("İ", "I"): "SGD",
                "SURİYE LİRASI".replace("İ", "I"): "SYP",
                "TAYLAND BAHTI".replace("İ", "I"): "THB",
                "YENİ TAYVAN DOLARI".replace("İ", "I"): "TWD",
                "UKRAYNA GRİVNASI".replace("İ", "I"): "UAH",
                "GRİVNA".replace("İ", "I"): "UAH",
                "URUGUAY PESOSU": "UYU",
                "GÜRCİSTAN LARİSİ".replace("İ", "I"): "GEL",
                "LARİ".replace("İ", "I"): "GEL",
                "TÜRK LİRASI".replace("İ", "I"): "TRY",
                "LİRA".replace("İ", "I"): "TRY",
                "TL": "TRY"
            }

            try:
                print(hitap + ": " + girdi_birim)
                birim = currency_dict[girdi_birim]
                print("Çevirilecek Birim: " + birim)
            
            except:
                x = "Lütfen geçerli bir para birimi ile daha sonra tekrar deneyiniz."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()

        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Çevirileceği birimi söyler misin?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            cikti_birim = ""
            cikti_birim = r.recognize_google(ses, language="tr-tr")
            cikti_birim = cikti_birim.upper()

            currency_dict = {
                "DOLAR": "USD",
                "AMERİKAN DOLARI".replace("İ", "I"): "USD",
                "EURO": "EUR",
                "STERLİN".replace("İ", "I"): "GBP", 
                "POUND": "GBP",
                "İNGİLİZ STERLİNİ".replace("İ", "I"): "GBP",
                "İNGİLİZ POUNDU".replace("İ", "I"): "GBP",
                "İSVİÇRE FRANGI".replace("İ", "I"): "CHF",
                "FRANK": "CHF",
                "KANADA DOLARI": "CAD",
                "RUBLE": "RUB",
                "RUS RUBLESİ".replace("İ", "I"): "RUB",
                "BİRLEŞİK ARAP EMİRLİKLERİ DİRHEMİ".replace("İ", "I"): "AED",
                "DİRHEM".replace("İ", "I"): "AED",
                "AVUSTRALYA DOLARI": "AUD",
                "DANİMARKA KRONU".replace("İ", "I"): "DKK",
                "KRON": "DKK",
                "İSVEÇ KRONU".replace("İ", "I"): "SEK",
                "NORVEÇ KRONU": "NOK",
                "JAPON YENİ".replace("İ", "I"): "JPY",
                "YEN": "JPY",
                "KUVEYT DİNARI".replace("İ", "I"): "KWD",
                "DİNAR".replace("İ", "I"): "KWD",
                "GÜNEY AFRİKA RANDI".replace("İ", "I"): "ZAR",
                "BAHREYN DİNARI".replace("İ", "I"):"BHD",
                "LİBYA DİNARI".replace("İ", "I"): "LYD",
                "SUUDİ ARABİSTAN RİYALİ".replace("İ", "I"): "SAR",
                "RİYAL".replace("İ", "I"): "SAR",
                "IRAK DİNARI".replace("İ", "I"): "IQD",
                "İSRAİL ŞEKELİ".replace("İ", "I"): "ILS",
                "İRAN RİYALİ".replace("İ", "I"): "IRR",
                "HİNDİSTAN RUPİSİ".replace("İ", "I"): "INR",
                "RUPİ".replace("İ", "I"): "INR",
                "MEKSİKA PESOSU".replace("İ", "I"): "MXN",
                "PESO": "MXN",
                "MACAR FORİNTİ".replace("İ", "I"): "HUF",
                "YENİ ZELANDA DOLARI".replace("İ", "I"): "NZD",
                "BREZİLYA REALİ".replace("İ", "I"): "BRL",
                "ENDONEZYA RUPİAHİ".replace("İ", "I"): "IDR",
                "ÇEK KORUNASI": "CSK",
                "POLONYA ZLOTİSİ".replace("İ", "I"): "PLN",
                "ZLOTİ".replace("İ", "I"): "PLN",
                "ZLOTY": "PLN",
                "ROMANYA LEYİ".replace("İ", "I"): "RON",
                "ÇİN YUANI".replace("İ", "I"): "CNY",
                "ARJANTİN PESOSU".replace("İ", "I"): "ARS",
                "ARNATUVLUK LEKİ".replace("İ", "I"): "ALL",
                "AZERBAYCAN MANATI": "AZN",
                "MANAT": "AZN",
                "BOSNA HERSEK MARKI".replace("İ", "I"): "BAM",
                "ŞİLİ PESOSU".replace("İ", "I"): "CLP",
                "KOLOMBİYA PESOSU".replace("İ", "I"): "COP",
                "KOSTA RİKA KOLONU".replace("İ", "I"): "CRC",
                "HONG KONG DOLARI": "HKD",
                "CEZAYİR DİNARI".replace("İ", "I"): "DZD",
                "MISIR LİRASI".replace("İ", "I"): "EGP",
                "ÜRDÜN DİNARI".replace("İ", "I"): "JOD",
                "HIRVAT KUNASI": "HRK",
                "İZLANDA KRONASI".replace("İ", "I"): "ISK",
                "GÜNEY KORE WONU": "KRW",
                "KAZAK TENGESİ".replace("İ", "I"): "KZT",
                "LÜBNAN LİRASI".replace("İ", "I"): "LBP",
                "SRİ LANKA RUPİSİ".replace("İ", "I"): "LKR",
                "FAS DİRHEMİ".replace("İ", "I"): "MAD",
                "MOLDOVYA LEUSU".replace("İ", "I"): "MDL",
                "MAKEDON DİNARI".replace("İ", "I"): "MKD",
                "MALEZYA RİNGGİTİ".replace("İ", "I"): "MYR",
                "UMMAN RİYALİ".replace("İ", "I"): "OMR",
                "PERU İNTİ".replace("İ", "I"): "PEN",
                "FİLİPİNLER PESOSU".replace("İ", "I"): "PHP",
                "PAKİSTAN RUPİSİ".replace("İ", "I"): "PKR",
                "KATAR RİYALİ".replace("İ", "I"): "QAR",
                "SIRBİSTAN DİNARI".replace("İ", "I"): "RSD",
                "SİNGAPUR DOLARI".replace("İ", "I"): "SGD",
                "SURİYE LİRASI".replace("İ", "I"): "SYP",
                "TAYLAND BAHTI".replace("İ", "I"): "THB",
                "YENİ TAYVAN DOLARI".replace("İ", "I"): "TWD",
                "UKRAYNA GRİVNASI".replace("İ", "I"): "UAH",
                "GRİVNA".replace("İ", "I"): "UAH",
                "URUGUAY PESOSU": "UYU",
                "GÜRCİSTAN LARİSİ".replace("İ", "I"): "GEL",
                "LARİ".replace("İ", "I"): "GEL",
                "TÜRK LİRASI".replace("İ", "I"): "TRY",
                "LİRA".replace("İ", "I"): "TRY",
                "TL": "TRY"
            }

            try:
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = currency_dict[cikti_birim]
                print("Çevirilecek Birim: " + cevirilecegi_birim)
            
            except:
                x = "Lütfen geçerli bir para birimi ile daha sonra tekrar deneyiniz."
                print("Bernard: " + x)
                Komut.konus(x)
                sys.exit()
 

        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Çevirilecek miktarı söyler misin?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            miktar = ""
            miktar = r.recognize_google(ses, language="tr-tr")
            miktar = miktar.replace(".", "")
            miktar = int(miktar)
            print(hitap + ": " + str(miktar))

        except sr.UnknownValueError:
            x = "Özür dilerim. Ne dediğini anlayamadığım için komutu tekrar çağırman gerekiyor."
            print("Bernard: " + x)
            Komut.konus(x)
            sys.exit()
            
        def cevir(cevirilecek_birim, cevirilecegi_birim, miktar): 
            cevirilecek_miktar = miktar
            access_key = "69648237ad8de22a76f205e41965c11b"
            url = str("http://data.fixer.io/api/latest?access_key=" + access_key)    
            oranlar = {}  
            data = requests.get(url).json() 
            oranlar = data["rates"]

            if cevirilecegi_birim != 'EUR' : 
                miktar = miktar / oranlar[cevirilecek_birim] 

            miktar = round(miktar * oranlar[cevirilecegi_birim], 2) 
            x = '{} {} = {} {}'.format(cevirilecek_miktar, cevirilecek_birim, str(miktar), cevirilecegi_birim)
            print(x)
            Komut.konus(x)
        
        cevir(birim, cevirilecegi_birim, miktar) 

    def hava_durumu():

        with sr.Microphone() as source:
            time.sleep(1)
            sor = "Hangi günün hava durumuna bakmak istiyorsunuz?"
            print("Bernard: " + sor)
            Komut.konus(sor)
            ses = r.listen(source)

        try:
            cevap = ""
            cevap = r.recognize_google(ses, language="tr-tr")
            print(hitap + ": " + cevap.capitalize())

        except:
            x = "Ne dediğini anlayamadım, lütfen daha sonra tekrar dene."
            print("Bernard: " + x)
            Komut.konus(x)

        
        if cevap.upper() == "BUGÜN":
            with sr.Microphone() as source:
                time.sleep(1)
                sor = "Hangi şehrin hava durumuna bakmak istiyorsun?"
                print("Bernard: " + sor)
                Komut.konus(sor)
                ses = r.listen(source)

            try:
                sehir = ""
                sehir = r.recognize_google(ses, language="tr-tr")
                print(hitap + ": " + sehir)

            except:
                x = "Hangi şehri istediniz anlayamadım, daha sonra tekrar deneyiniz."
                print("Bernard: " + x)
                Komut.konus(x)
                
            try:

                hava_durumu_json = json_getir_bugun(sehir)

                sicaklik = hava_durumu_json.get("main").get("temp")
                hissedilen_sicaklik = hava_durumu_json.get("main").get("feels_like")
                basinc = hava_durumu_json.get("main").get("pressure")
                nem = hava_durumu_json.get("main").get("humidity")

                sicaklik = kelvin_donusturucu(sicaklik)
                hissedilen_sicaklik = kelvin_donusturucu(hissedilen_sicaklik)

                x = "{} şehrinin hava durumu: \nSıcaklık: {} °C\nHissedilen Sıcaklık: {} °C\nBasınç: {} hPa\nNem: %{}".format(sehir, sicaklik, hissedilen_sicaklik, basinc, nem)

                print(x)
                Komut.konus(x)

            except AttributeError:
                x = "Geçersiz şehir, lütfen tekrar dene."
                print("Bernard: " + x)
                Komut.konus(x)

        else:
            bugun = date.today()
            cevap = tarih_bul(cevap)
            delta = cevap - bugun
            gun_farki = delta.days

            if gun_farki <= 14:
                with sr.Microphone() as source:
                    time.sleep(1)
                    sor = "Hangi şehrin hava durumuna bakmak istiyorsun?"
                    print("Bernard: " + sor)
                    Komut.konus(sor)
                    ses = r.listen(source)

                try:
                    sehir = ""
                    sehir = r.recognize_google(ses, language="tr-tr")
                    print(hitap + ": " + sehir)

                    path = "C:\Program Files (x86)\chromedriver.exe"
                    driver = webdriver.Chrome(path)

                    time.sleep(1)

                    driver.get("https://www.havadurumu15gunluk.net")

                    time.sleep(1)

                    driver.maximize_window()

                    time.sleep(1)

                    arama_bari = driver.find_element_by_xpath("//*[@id='query']")
                    arama_bari.send_keys(Keys.CONTROL + "a")
                    arama_bari.send_keys(Keys.DELETE)

                    time.sleep(1)

                    arama_bari.send_keys(sehir)
                    arama_bari.send_keys(Keys.ENTER)

                    time.sleep(3)

                    try:
                        hava_durumu_linki = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[3]/td[3]/table/tbody/tr[1]/td[2]/a")
                        hava_durumu_linki.click()
                        gun_farki = str(gun_farki + 1)

                        time.sleep(1)
                        xpath = "/html/body/table[4]/tbody/tr[3]/td[3]/table[" + gun_farki + "]"

                        durum = driver.find_element_by_xpath(xpath + "/tbody/tr[1]/td[4]/div").text                 
                        gunduz_sicaklik = driver.find_element_by_xpath(xpath+ "/tbody/tr[1]/td[5]").text.replace(" ", "")   
                        gece_sicaklik = driver.find_element_by_xpath(xpath + "/tbody/tr[1]/td[6]").text.replace(" ", "")   

                        x = "{} şehrinin hava durumu: \nHava Durumu: {}\nGündüz Sıcaklık: {}\nGece Sıcaklık: {}".format(sehir, durum, gunduz_sicaklik, gece_sicaklik)
                        print(x)
                        Komut.konus(x)

                    except:
                        x = "Lütfen geçerli bir şehir giriniz."
                        print("Bernard: " + x)
                        Komut.konus(x)

                except:
                    x = "Hangi şehri istediniz anlayamadım, daha sonra tekrar deneyiniz."
                    print("Bernard: " + x)
                    Komut.konus(x)
            else:
                x = "Lütfen 14 gün veya daha kısa bir süre söyleyiniz."
                print("Bernard: " + x)
                Komut.konus(x)

    def internet_hizi():
        st = speedtest.Speedtest()

        indirme = st.download()
        indirme = indirme / 10 ** 6
        indirme = round(indirme, 2)
        x = "İndirme hızınız: {} Mbps".format(indirme)
        print(x)
        Komut.konus(x)

        yukleme = st.upload()
        yukleme = yukleme / 10 ** 6
        yukleme = round(yukleme, 2)
        x = "Yükleme hızınız: {} Mbps".format(yukleme)
        print(x)
        Komut.konus(x)

        servernames =[]   
        st.get_servers(servernames)   
        ping = st.results.ping
        ping = int(ping)
        
        x = "Pinginiz: {}ms".format(ping)
        print(x)
        Komut.konus(x)

    def bilgilendirme_olustur():

        Komut.konus("Bilgilendirme süresi giriniz.")
        sure = input("Bilgilendirme süresi giriniz: ")
        sure = int(sure)
        
        Komut.konus("Bilgilendirme içeriği giriniz: ")
        icerik = input("Bilgilendirme içeriği giriniz: ")

        bilgilendirme = ToastNotifier()
        bilgilendirme.show_toast("Bernard", icerik, duration=sure)

    

    def komut_say():
        x = "Komutlarıma bu bağlantıdan ulaşabilirsin: "
        print("Bernard: " + x + "https://github.com/ardauzunoglu/Bernard")
        Komut.konus(x)

    def komut_bul(data):

        global e

        data = data.upper()
        
        if data == "KAPAT":
            Komut.kapat()

        elif data == "KOMUT SAY":
            Komut.komut_say()

        elif data == "TARİH".replace("İ", "I"):
            Komut.tarih()

        elif data == "NETFLİX".replace("İ", "I"):
            Komut.netflix()

        elif data == "ETKİNLİK GÖSTER".replace("İ", "I"):
            service = Komut.google_giris()

            gun = Komut.gun_sayisi_al()
            Komut.etkinlik_goster(gun, service)

        elif data == "GMAİL".replace("İ", "I"):
            Komut.gmail()

        elif data == "SPOTİFY".replace("İ", "I"):
            Komut.spotify()
            
        elif data == "ETKİNLİK EKLE".replace("İ", "I"):
            if e == 0:
                e += 1
                x = "Biraz sonra belirecek linke gidip uygulamaya izin vermelisiniz. Bu uygulama doğrulanmadı sekmesinde 'Gelişmiş' butonuna tıklayın ve alt tarafta yer alan uygulamaya gitme butonuna tıklayıp uygulamamıza izin verin. Daha sonrasında çıkan kodu kopyalıp terminal kısmına yapıştırın. Bu izni uygulamayı her açışınızda bir kere vermeniz yeterli olacaktır."
                print("Bernard: " + x)
                Komut.konus(x)

                calendar_id, service = Komut.google_auth()
                Komut.etkinlik_ekle()

                return e
                
            else: 
                Komut.etkinlik_ekle()

        elif data == "DÖVİZ ÇEVİR".replace("İ", "I"):
            Komut.doviz_cevir()

        elif data == "YOUTUBE":
            Komut.youtube()

        elif data == "YEMEKSEPETİ".replace("İ", "I"):
            Komut.yemeksepeti()

        elif data == "YEMEK SEPETİ".replace("İ", "I"):
            Komut.yemeksepeti()

        elif data == "GOOGLE":
            Komut.google()

        elif data == "ÇEVİRİ".replace("İ", "I"):
            Komut.ceviri()

        elif data == "HAVA DURUMU":
            Komut.hava_durumu()

        elif data == "VİKİPEDİ".replace("İ", "I"):
            Komut.vikipedi()

        elif data == "WHATSAPP":
            Komut.whatsapp()

        elif data == "İNTERNET HIZI".replace("İ", "I"):
            Komut.internet_hizi()

        elif data == "BİLGİLENDİRME OLUŞTUR".replace("İ", "I"):
            Komut.bilgilendirme_olustur()

        else:
            x = "Üzgünüm, geçersiz komut."
            print("Bernard: " + x)
            Komut.konus(x)

global hitap

hitap = Komut.kayit_ol()[2]        