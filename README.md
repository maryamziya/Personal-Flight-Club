# Personal Flight Club ✈️

Personal Flight Club is an automated flight price tracker that searches for cheap flights and sends low-price alerts directly to your WhatsApp. It monitors a list of dream destinations and compares current market prices with your target "lowest price."

## ✨ Features

- **Automated Flight Search**: Periodically checks for flights using the Amadeus API.
- **Dynamic Destination Management**: Uses Google Sheets (via Sheety) to manage destinations and target prices.
- **WhatsApp Alerts**: Sends instant notifications using Twilio WhatsApp API when a deal is found.
- **Smart Data Structuring**: Extracts and parses the most relevant flight information including origin, destination, dates, and prices.

## 🛠️ Technology Stack

- **Python**: Core logic and integration.
- **Amadeus API**: Real-time flight search data.
- **Sheety API**: Integration with Google Sheets for data management.
- **Twilio API**: WhatsApp messaging service for alerts.
- **Dotenv**: Secure environment variable management.

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/maryamziya/Personal-Flight-Club.git
cd Personal-Flight-Club
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory and add the following keys:
```env
token=YOUR_SHEETY_BEARER_TOKEN
sheety_url=YOUR_SHEETY_API_ENDPOINT
AMADEUS_API_KEY=YOUR_AMADEUS_API_KEY
AMADEUS_API_SECRET=YOUR_AMADEUS_API_SECRET
TWILIO_SID=YOUR_TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN
messaging_service_sid=YOUR_TWILIO_MESSAGING_SERVICE_SID
from_=whatsapp:YOUR_TWILIO_WHATSAPP_NUMBER
to=whatsapp:YOUR_PHONE_NUMBER
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Note: Ensure you have `requests`, `twilio`, and `python-dotenv` installed.)*

## 📖 Usage

Run the main script to start checking for flights:
```bash
python main.py
```

The script will:
1. Fetch your target destinations from Google Sheets.
2. Search for the cheapest flights within the next 6 months.
3. If a flight is found below your threshold, it sends a WhatsApp alert.

## 📂 Project Structure

- `main.py`: Entry point for the application. Coordinates data flow between search and notifications.
- `data_manager.py`: Handles interactions with the Sheety API (Google Sheets).
- `flight_search.py`: Manages authentication and queries for the Amadeus Flight API.
- `flight_data.py`: Structures and parses flight search results to find the best deals.
- `notification_manager.py`: Handles sending WhatsApp alerts via Twilio.

---
*Created with ❤️ for travelers looking for the best deals.*
