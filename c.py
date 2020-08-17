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
from nltk.chat.util import Chat, reflections

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

ciftler = [
    ["Benim adım (.*)", ["Selam %1, burada olduğun için çok mutluyum.", "Merhaba %1", "%1, ne güzel bir isim!"]],
    ["Bana (.*) diyebilirsin", ["Selam %1, burada olduğun için çok mutluyum.", "Merhaba %1", "%1, ne güzel bir isim!"]],
    ["Ben (.*)", ["Selam %1, burada olduğun için çok mutluyum.", "Merhaba %1", "%1, ne güzel bir isim!"]],

    ["Selam|Ne haber|Orada mısın?|Merhaba|İyi günler|Bernard", ["Merhaba!", "Seni görmek ne hoş!", "Selam, nasıl yardımcı olabilirim?"]],

    ["Elveda|Sonra görüşürüz|Görüşürüz|Ben çıkıyorum|İyi günler", ["Gitmen çok üzücü, görüşürüz. Beni kapatmak istiyorsan 'Kapat' demelisin", "Tamam, tekrar uğramayı unutma. Beni kapatmak istiyorsan 'Kapat' demelisin", "Görüşürüz! Beni kapatmak istiyorsan 'Kapat' demelisin"]],

    ["Adın ne|Sana nasıl hitap etmeliyim|İsmin ne|Sen nasıl çağırmalıyım|Bana ismini söyler misin", ["Bana Bernard diyebilirsin", "Adım Bernard", "Adım Bernard, babam adımı çok sevdiğini söyler hep."]],

    ["Neler yapabilirsin|Yeteneklerin neler|Ne hizmeti veriyorsun|Ne işe yarıyorsun", ["Yemek siparişi verebilirim! Detaylar için 'Bernard Detayları' demen yeterli.", "Takvimine etkinlik ekleyebilir, yaklaşan etkinliklerin gösterebilirim! Detaylar için 'Bernard Detayları' demen yeterli.", "Youtube'dan istediğin bir videoyu oynatabilirim! Detaylar için 'Bernard Detayları' demen yeterli.", "Netflix'ten istediğin bir içeriği açabilirim! Detaylar için 'Bernard Detayları' demen yeterli.", "Spotify'dan istediğin bir şarkıyı açabilirim! Detaylar için 'Bernard Detayları' demen yeterli.", "Wikipedia'dan istediğin bir bilgiyi getirebilirim! Detaylar için 'Bernard Detayları' demen yeterli.", "İnternette arama yapabilirim! Detaylar için 'Bernard Detayları' demen yeterli.", "Çeşitli alışveriş sitelerinde istediğin ürünü arayabilirim! Detaylar için 'Bernard Detayları' demen yeterli."]],

]

girdi = ses_al().lower()
sohbet = Chat(soylenilen, reflections)
sohbet.converse(quit = "Kapat")


