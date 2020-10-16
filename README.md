# Bernard


### Purpose 

Bernard is a voice assistant developed with gTTS. It can fulfill basic and simple tasks you give.

### Libraries Used

- datetime
- time
- speedtest
- playsound
- speech_recognition 
- sqlite3
- pytz
- smtplib
- requests
- wikipedia
- pyqrcode
- random
- pandas
- covid
- win10toast
- gtts
- selenium

### Requirements

> You must install the libraries in cmd using the command "pip install xxxxx".

> You must have the files in 'Other Files' in your Python path.

> You must install ChromeDriver and the directory shall be "C:\Program Files (x86)\chromedriver.exe".

[Download ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/)

> You must have the JSON files in your Python path.

[More about Python path](https://www.youtube.com/watch?v=Y2q_b4ugPWk)

[Needed JSON file 1 - credentials.json](https://developers.google.com/calendar/quickstart/go)

> Click 'Enable the Google Calendar API' button.

> Choose or create a project. Click Next.

> Choose desktop app. Click Create.

> Click 'DOWNLOAD CLIENT CONFIGURATION'.

[Needed JSON file 2 - client_secret.json](https://console.developers.google.com/apis/dashboard)

> Click 'Credentials'.

> Click 'Create credentials'.

> Choose OAuth.

> Choose Desktop app as application type. Create the credential.

> Click the download icon near to your OAuth credential.

### Commands - What can Bernard do?

**Command Name:** tarih <br>
**Function:** Returns and tells the date of asked day. <br>
**Example:** What is the date after 15 days? <br>

**Command Name:** netflix <br>
**Function:** Asks you, which content you want it to play, and then opens the website of Netflix and plays the content. <br>

**Command Name:** spotify <br>
**Function:** Opens the web player of Spotify and plays the latest song you have played on any device. <br>

**Command Name:** yemeksepeti <br>
**Function:** Asks you the name of the restaurant you want to order from and three items from the restaurant, and then orders the items -you can order less than three items if you want- from Yemeksepeti. <br>

**Command Name:** gmail <br>
**Function:** Asks you the email address of receiver, title of the email and the message you want to send, and then sends the email with the given information. <br>

**Command Name:** youtube <br>
**Function:** Asks the video you want it to play, searchs the input you give, and plays the first result of search. If the first result of the search is a channel, it automatically opens the videos section of that channel. <br>

**Command Name:** google <br>
**Function:** Googles anything you say and returns the first result of the search whether it is a explanation, wikipedia bar, youtube video or a regular link. It plays the youtube video if it is the first result. <br>

**Command Name:** ceviri <br>
**Function:** Translates any word you want from Turkish to the language you want between English, German and Spanish. <br>

**Command Name:** etkinlik_goster <br>
**Function:** Asks you the amount of the days you want to look for if there is an activity on Google Calendar, and returns all the activities if there are any. <br>

**Command Name:** etkinlik_ekle <br>
**Function:** Adds a new activity to Google Calendar in the direction of the information given by you. <br>

**Command Name:** doviz_cevir <br>
**Function:** Converts between more than 50 currencies. <br>

**Command Name:** hava_durumu <br>
**Function:** Shows the weather forecast of both the current day and a day you want in a 14 days range. <br>

**Command Name:** vikipedi <br>
**Function:** You can search anything that you can search on Wikipedia with this command. Bernard brings up results of your search. <br>

**Command Name:** whatsapp <br>
**Function:** Bernard asks you to who you want to message and what do you want to message and then sends the message. <br>

**Command Name:** internet_hizi <br>
**Function:** Measures your Ping with Download and Upload Mbps'. <br>

**Command Name:** bilgilendirme_olustur <br>
**Function:** Creates a Windows notification with a duration you want. <br>

**Command Name:** qr_kod_olustur <br>
**Function:** Creates a QR code that directs you to a url you want. <br>

**Command Name:** sifre_olustur <br>
**Function:** Creates a password that includes letters and/or symbols you want with a length of your preference. <br>

**Command Name:** coronavirus <br>
**Function:** Brings data about COVID-19. <br>

**Command Name:** eksi_sozluk <br>
**Function:** Collects and stores data from a headline from Ekşi Sözlük platform. <br>

### Developer 

Arda Uzunoğlu - [ardauzunoglu](https://github.com/ardauzunoglu)

### Further Notes

Error handling can and should be improved.

Various and better commands are on the way. Stay tuned!

Latest Update: 26 September 2020

### Amaç 

Bernard gTTS kullanılarak geliştirilen bir sesli asistan. Verdiğiniz basit, belli başlı görevleri gerçekleştirir.

### Kullanılan Kütüphaneler

- datetime
- time
- speedtest
- playsound
- speech_recognition 
- sqlite3
- pytz
- smtplib
- requests
- wikipedia
- pyqrcode
- random
- pandas
- covid
- win10toast
- gtts
- selenium

### Gereksinimler

> Yukarıdaki kütüphaneleri konsolda "pip install xxxxx" komudu ile kurmalısınız.

> 'Other Files'daki dosyalar Python path'inizde olmalı.

> ChromeDriver'ı kurmalısınız ve konumu "C:\Program Files (x86)\chromedriver.exe" olmalı.

[ChromeDriver'ı İndir](https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/)

> JSON dosyaları Python'ın path'inde olmalı.

[Python path'i hakkında daha fazlası](https://www.youtube.com/watch?v=Y2q_b4ugPWk)

[Gerekli JSON dosyası 1 - credentials.json](https://developers.google.com/calendar/quickstart/go)

> 'Enable the Google Calendar API' butonuna tıklayın.

> Bir proje seçin ya da yeni bir proje oluşturun. Next butonuna tıklayın.

> Desktop app'i seçin. Create butonuna tıklayın.

> 'DOWNLOAD CLIENT CONFIGURATION' butonuna tıklayın.

[Needed JSON file 2 - client_secret.json](https://console.developers.google.com/apis/dashboard)

> Kimlik bilgilerine tıklayın.

> 'Kimlik bilgisi oluştur' butonuna tıklayın.

> OAuth işlemci kimliğini seçin.

> Uygulama türü olarak masaüstü uygulamasını seçin. 'Oluştur' butonuna tıklayın.

> Oluşturduğunuz yeni işlemci kimliğinin yanındaki indirme ikonuna tıklayın.

### Komutlar - Bernard neler yapabilir?

**Komut Adı:** tarih <br>
**İşlev:** Sorduğunuz günün tarihini söyler. <br>
**Örnek:** 15 gün sonrasının tarihi ne? <br>

**Komut Adı:** netflix <br>
**İşlev:** Açmak istediğiniz içeriği sorar ve Netflix'in websitesine girerek o içeriği oynatır. <br>

**Komut Adı:** spotify <br>
**İşlev:** Spotify'ın web player'ına girerek herhangi bir cihazda dinlediğiniz en son şarkıyı oynatır. <br>

**Komut Adı:** yemeksepeti <br>
**İşlev:** Sipariş etmek istediğiniz restoranı ve o restorandan sipariş edeceğiniz üç parçayı -daha azını da sipariş edebilirsiniz- sorar ve Yemeksepeti üzerinden sipariş verir. <br>

**Komut Adı:** gmail <br>
**İşlev:** Alıcının eposta adresini, epostanın başlığını ve göndermek istediğiniz mesajı sorar ve verdiğiniz bilgiler doğrultusunda eposta gönderir. <br>

**Komut Adı:** youtube <br>
**İşlev:** Açmak istediğiniz videoyu sorar, arama yapar ve arama sonucu çıkan ilk videoyu açar. Eğer arama sonucu çıkan ilk şey bir kanalsa, o kanalın videolar sekmesini açar. <br>

**Komut Adı:** google <br>
**İşlev:** İstediğiniz herhangi bir şeyi Google'lar ve çıkan sonuç ister bir açıklama, ister bir vikipedi barı, ister bir youtube videosu, ister sıradan bir bağlantı olsun, bu sonucu döndürür ve sana söyler. Eğer çıkan ilk sonuç bir youtube videosu ise o videoyu açar. <br>

**Komut Adı:** ceviri <br>
**İşlev:** Türkçe'den, İngilizce, Almanca ya da İspanyolca dillerinden istediğinize kelime çevirisi yapar. <br>

**Komut Adı:** etkinlik_goster <br>
**İşlev:** Google Calendar üzerinden istediğiniz gün sayısı içerisindeki etkinliklerinizi gösterir. <br>

**Komut Adı:** etkinlik_ekle <br>
**İşlev:** Google Calendar'a verdiğiniz bilgiler doğrultusunda yeni bir etkinlik ekler. <br>

**Komut Adı:** doviz_cevir <br>
**İşlev:** 50'den fazla para birimi arasında çeviri yapar. <br>

**Komut Adı:** hava_durumu <br>
**İşlev:** Hem içinde bulunduğunuz hem de 14 gün içerisinde istediğiniz bir günün hava durumunu gösterir. <br>

**Komut Adı:** vikipedi <br>
**İşlev:** Vikipedi üzerinde yapacağınız herhangi bir aramayı bu komut ile gerçekleştirebilirsiniz. Bernard yaptığınız aramanın sonuçlarını getirir. <br>

**Komut Adı:** whatsapp <br>
**İşlev:** Bernard, kime mesaj göndereceğinizi ve göndereceğiniz mesajı sorar ve mesajı gönderir. <br>

**Komut Adı:** internet_hizi <br>
**İşlev:** Pinginiz ile Yükleme ve İndirme Mbps'lerinizi ölçer. <br>

**Komut Adı:** bilgilendirme_olustur <br>
**İşlev:** İstediğiniz kadar sürecek bir Windows bildirimi oluşturur. <br>

### Geliştirici 

Arda Uzunoğlu - [ardauzunoglu](https://github.com/ardauzunoglu)

### İlave Notlar

Hata ayıklaması daha iyi yapılabilir/yapılmalı.

Çeşitli ve daha iyi komutlar yolda. Takipte kalın!

Son Güncelleme: 26 Eylül 2020
