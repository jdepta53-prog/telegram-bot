import os
import time
import requests
import xml.etree.ElementTree as ET
from telegram import Bot

# Konfiguracja - nazwa Twojej grupy i token bota
GROUP_SHARE_LINK = "@MojaGrupaBetLab123"

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Darmowe źródło typów (Feed RSS z analizami i typami)
RSS_URL = "https://www.olbg.com/rss/blogs"

def get_latest_tip():
    try:
        response = requests.get(RSS_URL, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            # Pobieramy pierwszy, najnowszy wpis
            item = root.find(".//item")
            if item is not None:
                title = item.find("title").text
                link = item.find("link").text
                description = item.find("description").text
                # Proste oczyszczanie tekstu z tagów HTML jeśli istnieją
                if "<" in description:
                    description = description.split("<")[0]
                return title, description, link
    except Exception as e:
        print(f"Błąd podczas pobierania typów: {e}")
    return None

def main():
    if not TOKEN:
        print("Brak tokenu bota w zmiennych środowiskowych!")
        return

    bot = Bot(token=TOKEN)
    print("Bot automatyczny BetLab uruchomiony...")
    
    last_title = ""

    while True:
        tip_data = get_latest_tip()
        
        if tip_data:
            title, description, link = tip_data
            
            # Jeśli to nowy typ, którego jeszcze nie wysyłaliśmy
            if title != last_title:
                last_title = title
                
                # Tworzymy ładny, automatyczny szablon wiadomości
                message = (
                    "🎯 **NOWY AUTOMATYCZNY TYP OD BETLAB!** 🎯\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚽️ **Mecz/Analiza:** {title}\n\n"
                    f"📝 **Szczegóły:** {description[:200]}...\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    f"🔗 [Zobacz pełną analizę]({link})\n"
                    "🍀 _Powodzenia!_"
                )
                
                try:
                    bot.send_message(chat_id=GROUP_SHARE_LINK, text=message, parse_mode="Markdown")
                    print(f"Wysłano nowy typ: {title}")
                except Exception as e:
                    print(f"Błąd wysyłania wiadomości: {e}")
                    
        # Czekaj 15 minut (900 sekund) przed kolejnym sprawdzeniem strony
        time.sleep(900)

if __name__ == "__main__":
    main()

