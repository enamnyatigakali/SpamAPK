![logo](SpamApk_1.png)
# Spam APK Tools
Ini adalah Tools Sederhana untuk melakukan Spam kepada Bot Penipuan APK yang marak saat ini.
Dengan Tools ini membantu pengguna untuk mengirimkan spam dengan mengonfigurasi ID Bot Token, Chat ID, pesan yang akan dikirim, dan jumlah pesan yang diinginkan sampai bot tidak bisa lagi menerima pesan sampai limit.

# Cara Mendapatkan BOT TOKEN dan CHAT ID Target
1. Buka APK dengan Applikasi JADX (https://github.com/skylot/jadx)
2. Search variabel "api.telegram" untuk mendapatkan BOT TOKEN dan CHAT ID Target.
![logo](Get%20ID%20Bot.png)
Example : https://.api.telegram.org/bot [BOT_TOKEN] /sendMessage?parse_mode=markdown&chat_id= [CHAT_ID]

# Cara Menggunakan
1. Clone Repository
2. jalankan script spamapk.py
3. Masukkan ID Bot Token dan Chat ID Target.
4. Masukkan pesan yang akan dikirim.
5. Tentukan jumlah pesan yang ingin dikirim.
6. Script akan mengirim pesan sesuai dengan input yang diberikan.



