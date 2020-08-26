# Bernard


### Purpose 

Bernard is a voice assistant developed with gTTS. It can fulfill basic and simple tasks you give.

### Libraries Used

- speech_recognition
- time
- sys
- datetime
- pickle 
- os
- playsound
- sqlite3
- gTTS
- selenium
- smtplib
- requests

### Requirements

> You must install the libraries in cmd using the command "pip install xxxxx".

> You must have the JSON files in your Python path.

[More about Python path](https://www.youtube.com/watch?v=Y2q_b4ugPWk)

### Commands - What can Bernard do?

**Command Name:** tarih 
**Function:** Returns and tells the date of asked day.
**Example:** What is the date after 15 days?

**Command Name:** netflix
**Function:** Asks you, which content you want it to play, and then opens the website of Netflix and plays the content.

**Command Name:** spotify
**Function:** Opens the web player of Spotify and plays the latest song you have played on any device.

**Command Name:** yemeksepeti
**Function:** Asks you the name of the restaurant you want to order from and three items from the restaurant, and then orders the items -you can order less than three items if you want- from Yemeksepeti.

**Command Name:** gmail
**Function:** Asks you the email address of receiver, title of the email and the message you want to send, and then sends the email with the given information.

**Command Name:** youtube
**Function:** Asks the video you want it to play, searchs the input you give, and plays the first result of search. If the first result of the search is a channel, it automatically opens the videos section of that channel.

**Command Name:** google
**Function:** Googles anything you say and returns the first result of the search whether it is a explanation, wikipedia bar, youtube video or a regular link. It plays the youtube video if it is the first result.

**Command Name:** ceviri
**Function:** Translates any word you want from Turkish to the language you want between English, German and Spanish.

**Command Name:** etkinlik_goster
**Function:** Asks you the amount of the days you want to look for if there is an activity on Google Calendar, and returns all the activities if there are any.

**Command Name:** etkinlik_ekle
**Function:** Adds a new activity to Google Calendar in the direction of the information given by you.

**Command Name:** doviz_cevir
**Function:** Converts between more than 50 currencies.

### Developer 

Arda Uzunoğlu - [ardauzunoglu](https://github.com/ardauzunoglu)

### Further Notes

Error handling can and should be improved.

### Amaç 

Bernard gTTS kullanılarak geliştirilen bir sesli asistan. Verdiğiniz basit, belli başlı görevleri gerçekleştirir.

### Kullanılan Kütüphaneler

- speech_recognition
- time
- sys
- datetime
- pickle 
- os
- playsound
- sqlite3
- gTTS
- selenium
- smtplib
- requests

### Gereksinimler

> Yukarıdaki kütüphaneleri konsolda "pip install xxxxx" komudu ile kurmalısınız.

> JSON dosyaları Python'ın path'inde olmalı.

[Python path'i hakkında daha fazlası](https://www.youtube.com/watch?v=Y2q_b4ugPWk)

### Komutlar - Bernard neler yapabilir?

**Komut Adı:** tarih 
**Örnek:** Sorduğunuz günün tarihini söyler.
<br>
**Örnek:** 15 gün sonrasının tarihi ne?

**Komut Adı:** netflix
**Örnek:** Açmak istediğiniz içeriği sorar ve Netflix'in websitesine girerek o içeriği oynatır.

**Komut Adı:** spotify
**Örnek:** Spotify'ın web playerına girerek herhangi bir cihazda dinlediğiniz en son şarkıyı oynatır.

**Komut Adı:** yemeksepeti
**Örnek:** Sipariş etmek istediğiniz restoranı ve o restorandan sipariş edeceğiniz üç parçayı -daha azını da sipariş edebilirsiniz- sorar ve Yemeksepeti üzerinden sipariş verir.

**Komut Adı:** gmail
**Örnek:** Alıcının eposta adresini, epostanın başlığını ve göndermek istediğiniz mesajı sorar ve verdiğiniz bilgiler doğrultusunda eposta gönderir.

**Komut Adı:** youtube
**Örnek:** Açmak istediğiniz videoyu sorar, arama yapar ve arama sonucu çıkan ilk videoyu açar. Eğer arama sonucu çıkan ilk şey bir kanalsa, o kanalın videolar sekmesini açar.

**Komut Adı:** google
**Örnek:** İstediğiniz herhangi bir şeyi Google'lar ve çıkan sonuç ister bir açıklama, ister bir vikipedi barı, ister bir youtube videosu, ister sıradan bir bağlantı olsun, bu sonucu döndürür ve sana söyler. Eğer çıkan ilk sonuç bir youtube videosu ise o videoyu açar.

**Komut Adı:** ceviri
**Örnek:** Türkçe'den, İngilizce, Almanca ya da İspanyolca dillerinden istediğinize kelime çevirisi yapar.

**Komut Adı:** etkinlik_goster
**Örnek:** Google Calendar üzerinden istediğiniz gün sayısı içerisindeki etkinliklerinizi gösterir.

**Komut Adı:** etkinlik_ekle
**Örnek:** Google Calendar'a verdiğiniz bilgiler doğrultusunda yeni bir etkinlik ekler.

**Komut Adı:** doviz_cevir
**Örnek:** 50'den fazla para birimi arasında çeviri yapar.

### Developer 

Arda Uzunoğlu - [ardauzunoglu](https://github.com/ardauzunoglu)

### Further Notes

Hata ayıklaması daha iyi yapılabilir/yapılmalı.
