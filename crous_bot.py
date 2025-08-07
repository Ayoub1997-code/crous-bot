import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot

TOKEN = "8480400096:AAGr6kWcGLO7SUlc7BIjfdPbeAVQHaTYEKI"
CHAT_ID = "5653608572"

bot = Bot(token=TOKEN)
URL = "https://trouverunlogement.lescrous.fr/logement"

def get_offers():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    offers = []

    # عدل هذا الجزء بناءً على هيكل الموقع
    for offer_div in soup.find_all("div", class_="offre"):  # استبدل 'offre' بالكلاس الصحيح
        title = offer_div.find("h3").text.strip()
        description = offer_div.find("p").text.strip()
        offers.append(f"{title}\n{description}")

    return offers

def send_offers():
    offers = get_offers()
    if offers:
        message = "🏠 العروض المتاحة الآن:\n\n" + "\n\n".join(offers)
    else:
        message = "لا توجد عروض متاحة حالياً."
    bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    while True:
        send_offers()
        time.sleep(300)  # كل 5 دقائق

if __name__ == "__main__":
    main()

