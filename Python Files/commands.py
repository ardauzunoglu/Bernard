from __future__ import print_function
import datetime
import pickle
import os.path
import datetime
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
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import smtplib
from smtplib import SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import requests

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

            if girdi_birim == "DOLAR":
                print(hitap + ": " + girdi_birim)
                birim = "USD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "AMERİKAN DOLARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "USD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "EURO":
                print(hitap + ": " + girdi_birim)
                birim = "EUR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "STERLİN".replace("İ", "I"): 
                print(hitap + ": " + girdi_birim)
                birim = "GBP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "POUND": 
                print(hitap + ": " + girdi_birim)
                birim = "GBP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "İNGİLİZ STERLİNİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "GBP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "İNGİLİZ POUNDU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "GBP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "İSVİÇRE FRANGI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "CHF"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "FRANK":
                print(hitap + ": " + girdi_birim)
                birim = "CHF"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "KANADA DOLARI":
                print(hitap + ": " + girdi_birim)
                birim = "CAD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "RUBLE": 
                print(hitap + ": " + girdi_birim)
                birim = "RUB"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "RUS RUBLESİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "RUB"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "BİRLEŞİK ARAP EMİRLİKLERİ DİRHEMİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "AED"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "DİRHEM".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "AED"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "AVUSTRALYA DOLARI":
                print(hitap + ": " + girdi_birim)
                birim = "AUD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "DANİMARKA KRONU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "DKK"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "KRON":
                print(hitap + ": " + girdi_birim)
                birim = "DKK"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "İSVEÇ KRONU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "SEK"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "NORVEÇ KRONU":
                print(hitap + ": " + girdi_birim)
                birim = "NOK"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "JAPON YENİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "JPY"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "YEN":
                print(hitap + ": " + girdi_birim)
                birim = "JPY"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "KUVEYT DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "KWD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "DİNAR".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "KWD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "GÜNEY AFRİKA RANDI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "ZAR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "BAHREYN DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "BHD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "LİBYA DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "LYD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "SUUDİ ARABİSTAN RİYALİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "SAR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "RİYAL".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "SAR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "IRAK DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "IQD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "İSRAİL ŞEKELİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "ILS"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ŞEKEL":
                print(hitap + ": " + girdi_birim)
                birim = "ILS"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "İRAN RİYALİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "IRR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "RİYAL".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "IRR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "HİNDİSTAN RUPİSİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "INR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "RUPİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "INR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "MEKSİKA PESOSU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "MXN"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "PESO":
                print(hitap + ": " + girdi_birim)
                birim = "MXN"
                print("Çevirilecek Birim: " + birim)
            
            elif girdi_birim == "MACAR FORİNTİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "HUF"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "YENİ ZELANDA DOLARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "NZD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "BREZİLYA REALİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "BRL"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ENDONEZYA RUPİAHİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "IDR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ÇEK KORUNASI":
                print(hitap + ": " + girdi_birim)
                birim = "CSK"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "POLONYA ZLOTİSİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "PLN"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ZLOTİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "PLN"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ZLOTY":
                print(hitap + ": " + girdi_birim)
                birim = "PLN"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ROMANYA LEYİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "RON"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ÇİN YUANI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "CNY"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ARJANTİN PESOSU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "ARS"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ARNATUVLUK LEKİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "ALL"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "AZERBAYCAN MANATI":
                print(hitap + ": " + girdi_birim)
                birim = "AZN"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "MANAT":
                print(hitap + ": " + girdi_birim)
                birim = "AZN"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "BOSNA HERSEK MARKI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "BAM"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ŞİLİ PESOSU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "CLP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "KOLOMBİYA PESOSU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "COP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "KOSTA RİKA KOLONU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "CRC"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "HONG KONG DOLARI":
                print(hitap + ": " + girdi_birim)
                birim = "HKD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "CEZAYİR DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "DZD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "MISIR LİRASI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "EGP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "ÜRDÜN DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "JOD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "HIRVAT KUNASI":
                print(hitap + ": " + girdi_birim)
                birim = "HRK"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "İZLANDA KRONASI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "ISK"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "GÜNEY KORE WONU":
                print(hitap + ": " + girdi_birim)
                birim = "KRW"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "KAZAK TENGESİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "KZT"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "LÜBNAN LİRASI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "LBP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "SRİ LANKA RUPİSİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "LKR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "FAS DİRHEMİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "MAD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "MOLDOVYA LEUSU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "MDL"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "MAKEDON DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "MKD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "MALEZYA RİNGGİTİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "MYR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "UMMAN RİYALİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "OMR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "PERU İNTİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "PEN"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "FİLİPİNLER PESOSU".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "PHP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "PAKİSTAN RUPİSİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "PKR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "KATAR RİYALİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "QAR"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "SIRBİSTAN DİNARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "RSD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "SİNGAPUR DOLARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "SGD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "SURİYE LİRASI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "SYP"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "TAYLAND BAHTI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "THB"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "YENİ TAYVAN DOLARI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "TWD"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "UKRAYNA GRİVNASI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "UAH"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "GRİVNA".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "UAH"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "URUGUAY PESOSU":
                print(hitap + ": " + girdi_birim)
                birim = "UYU"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "GÜRCİSTAN LARİSİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "GEL"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "LARİ".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "GEL"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "TÜRK LİRASI".replace("İ", "I"):
                print(hitap + ": " + girdi_birim)
                birim = "TRY"
                print("Çevirilecek Birim: " + birim)

            elif girdi_birim == "TL":
                print(hitap + ": " + girdi_birim)
                birim = "TRY"
                print("Çevirilecek Birim: " + birim)

            else:
                x = "Lütfen komutu tekrar çağırıp geçerli bir para birimi ile tekrar deneyiniz."
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

            if cikti_birim == "DOLAR":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "USD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "AMERİKAN DOLARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "USD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "EURO":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "EUR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "STERLİN".replace("İ", "I"): 
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "GBP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "POUND": 
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "GBP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "İNGİLİZ STERLİNİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "GBP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "İNGİLİZ POUNDU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "GBP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "İSVİÇRE FRANGI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "CHF"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "FRANK":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "CHF"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "KANADA DOLARI":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "CAD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "RUBLE": 
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "RUB"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "RUS RUBLESİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "RUB"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "BİRLEŞİK ARAP EMİRLİKLERİ DİRHEMİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "AED"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "DİRHEM".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "AED"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "AVUSTRALYA DOLARI":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "AUD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "DANİMARKA KRONU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "DKK"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "KRON":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "DKK"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "İSVEÇ KRONU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "SEK"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "NORVEÇ KRONU":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "NOK"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "JAPON YENİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "JPY"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "YEN":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "JPY"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "KUVEYT DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "KWD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "DİNAR".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "KWD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "GÜNEY AFRİKA RANDI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "ZAR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "BAHREYN DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "BHD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "LİBYA DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "LYD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "SUUDİ ARABİSTAN RİYALİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "SAR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "RİYAL".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "SAR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "IRAK DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "IQD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "İSRAİL ŞEKELİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "ILS"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ŞEKEL":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "ILS"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "İRAN RİYALİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "IRR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "RİYAL".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "IRR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "HİNDİSTAN RUPİSİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "INR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "RUPİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "INR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "MEKSİKA PESOSU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "MXN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "PESO":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "MXN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)
            
            elif cikti_birim == "MACAR FORİNTİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "HUF"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "YENİ ZELANDA DOLARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "NZD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "BREZİLYA REALİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "BRL"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ENDONEZYA RUPİAHİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "IDR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ÇEK KORUNASI":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "CSK"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "POLONYA ZLOTİSİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "PLN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ZLOTİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "PLN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ZLOTY":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "PLN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ROMANYA LEYİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "RON"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ÇİN YUANI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "CNY"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ARJANTİN PESOSU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "ARS"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ARNATUVLUK LEKİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "ALL"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "AZERBAYCAN MANATI":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "AZN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "MANAT":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "AZN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "BOSNA HERSEK MARKI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "BAM"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ŞİLİ PESOSU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "CLP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "KOLOMBİYA PESOSU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "COP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "KOSTA RİKA KOLONU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "CRC"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "HONG KONG DOLARI":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "HKD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "CEZAYİR DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "DZD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "MISIR LİRASI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "EGP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "ÜRDÜN DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "JOD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "HIRVAT KUNASI":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "HRK"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "İZLANDA KRONASI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "ISK"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "GÜNEY KORE WONU":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "KRW"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "KAZAK TENGESİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "KZT"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "LÜBNAN LİRASI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "LBP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "SRİ LANKA RUPİSİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "LKR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "FAS DİRHEMİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "MAD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "MOLDOVYA LEUSU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "MDL"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "MAKEDON DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "MKD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "MALEZYA RİNGGİTİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "MYR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "UMMAN RİYALİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "OMR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "PERU İNTİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "PEN"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "FİLİPİNLER PESOSU".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "PHP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "PAKİSTAN RUPİSİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "PKR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "KATAR RİYALİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "QAR"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "SIRBİSTAN DİNARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "RSD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "SİNGAPUR DOLARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "SGD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "SURİYE LİRASI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "SYP"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "TAYLAND BAHTI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "THB"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "YENİ TAYVAN DOLARI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "TWD"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "UKRAYNA GRİVNASI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "UAH"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "GRİVNA".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "UAH"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "URUGUAY PESOSU":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "UYU"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "GÜRCİSTAN LARİSİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "GEL"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "LARİ".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "GEL"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "TÜRK LİRASI".replace("İ", "I"):
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "TRY"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            elif cikti_birim == "TL":
                print(hitap + ": " + cikti_birim)
                cevirilecegi_birim = "TRY"
                print("Çevirileceği Birim: " + cevirilecegi_birim)

            else:
                x = "Lütfen komutu tekrar çağırıp geçerli bir para birimi ile tekrar deneyiniz."
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
    
    def komut_say():
        x = "Komutlarımı çalıştırmak için adlarını söylemen yeterli. İşte komut listem: Komut Adı: Kapat. Komut İşlevi: Kendimi kapatırım. \nKomut Adı: Sipariş. Komut İşlevi: Yemeksepeti üzerinden yemek siparişi verebilirim. \nKomut Adı: Tarih. Komut İşlevi: İstediğin bir günün tarihini söyleyebilirim."
        print("Bernard: " + x)
        Komut.konus(x)

    def komut_bul(data):

        global e

        data = data.upper()
        
        if data == "KAPAT":
            Komut.kapat()

        elif data == "NE YAPARSIN":
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "NE YAPIYORSUN":
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "NE YAPABİLİRSİN".replace("İ","I"):
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "NE YAPABİLİYORSUN".replace("İ","I"):
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "NELER YAPARSIN":
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "NELER YAPIYORSUN":
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "NELER YAPABİLİRSİN".replace("İ","I"):
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "NELER YAPABİLİYORSUN".replace("İ","I"):
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

        elif data == "YETENEKLERİN NELER".replace("İ","I"):
            x = "Neler yapabileceğimi öğrenmek için komut say diyebilirsin."
            print("Bernard: " + x)
            Komut.konus(x)

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

        else:
            x = "Üzgünüm, geçersiz komut."
            print("Bernard: " + x)
            Komut.konus(x)

global hitap

hitap = Komut.kayit_ol()[2]        
