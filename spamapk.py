import pyfiglet 
import requests

enam = pyfiglet.figlet_format("SPAM APK", font = "slant"  )
sembilan = pyfiglet.figlet_format("By EnamnyaTigaKali", font = "term" )
print(enam,sembilan)

def send_telegram_message(bot_token, chat_id, message):
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message,
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        print("Pesan berhasil dikirim!")
    else:
        print(f"Terjadi kesalahan: {response.status_code}, {response.text}")

if __name__ == "__main__":
    bot_token = input("Masukkan Bot Token: ")
    chat_id = input("Masukkan Chat ID: ")
    message = input("Masukkan Pesan: ")
    
    try:
        num_messages = int(input("Berapa banyak pesan yang akan dikirim? "))
    except ValueError:
        print("Masukkan angka yang valid.")
        exit()

    for _ in range(num_messages):
        send_telegram_message(bot_token, chat_id, message)
