import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time

# 🛠️ أدخل هنا رمز البوت الخاص بك (Token) ومعرف المحادثة (chat_id)
TELEGRAM_TOKEN = '8480400096:AAGr6kWcGLO7SUlc7BIjfdPbeAVQHaTYEKI'
CHAT_ID = '5653608572'

# إعداد البوت
bot = Bot(token=TELEGRAM_TOKEN)
url = "https://trouverunlogement.lescrous.fr/logement"

# لتجنب تكرار نفس العروض
offres_vues = set()

print("🤖 Bot CROUS démarre...")

while True:
    try:
        print("🔍 Vérification des nouvelles offres...")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        offres = soup.find_all("a", class_="card-annonce")

        for offre in offres:
            lien = "https://trouverunlogement.lescrous.fr" + offre.get("href")
            titre = offre.get_text(strip=True)

            if lien not in offres_vues:
                offres_vues.add(lien)
                message = f"🏠 Offre logement CROUS:\n{titre}\n{lien}"
                bot.send_message(chat_id=CHAT_ID, text=message)
                print("✅ Nouvelle offre envoyée:", lien)

        print("⏸️ Attente de 1 heure avant la prochaine vérification...\n")
        time.sleep(3600)

    except Exception as e:
        print("⚠️ Une erreur est survenue:", e)
        time.sleep(300)  # Attendre 5 minutes avant de réessayer
