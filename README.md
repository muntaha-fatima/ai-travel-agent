# 🧳 AI Travel Agent

An AI-powered multi-agent system that helps users plan complete travel experiences — from selecting destinations to booking hotels and exploring local attractions. Built using **Chainlit**, **Gemini**, and structured with **Agent SDK-style logic**, this project includes multiple tools, agents, and handoff-based flows.

---

## ✅ Requirements Met

| Requirement                              | Implemented ✅ |
|------------------------------------------|----------------|
| Use at least **2 Tools**                 | ✅ `Book Flight`, `Book Hotel`, `Suggest Attractions` |
| Use at least **2 Agents**                | ✅ `PlannerAgent`, `FlightAgent`, `HotelAgent`, `AttractionAgent` *(4 total)* |
| Handoff Logic between Agents & Tools     | ✅ Implemented |
| Use of **OpenAI Agent SDK-style logic**  | ✅ Via `@tool`, `on_message`, modular agents |
| Well-structured code folder              | ✅ Yes |
| `README.md` with agent and flow details  | ✅ You're reading it! |

---

## 🌍 What This Agent Does

It helps users plan a full travel journey by:

1. Asking for preferences (mood, country, etc.)
2. Suggesting destinations and experiences
3. Booking mock **flights** and **hotels**
4. Recommending **local attractions**
5. Giving a summary travel plan

---

## 🔁 Flow Logic

```text
User Input →
  → PlannerAgent: interprets query
    → BookFlight Tool → FlightAgent handles flight booking
    → BookHotel Tool → HotelAgent handles hotels
    → SuggestAttractions Tool → AttractionAgent returns places to visit

```
📁 Project Structure

ai-travel-agent/
├── agents/
│   ├── planner_agent.py         # Main planner and coordinator
│   ├── flight_agent.py          # Handles flight booking
│   ├── hotel_agent.py           # Handles hotel booking
│   └── attraction_agent.py      # Suggests attractions
├── tools/
│   └── travel_tools.py          # Contains @tool methods like book_flight, book_hotel
├── main.py                      # Chainlit entry and logic handler
├── .env                         # Gemini API key
├── requirements.txt             # All dependencies
└── README.md                    # You're here!

``
🛠️ Tools Used


| Tool Name                  | Description                           |
| -------------------------- | ------------------------------------- |
| `book_flight_tool`         | Simulates a mock flight booking       |
| `book_hotel_tool`          | Books hotels based on destination     |
| `suggest_attractions_tool` | Suggests tourist spots or experiences |

``
👥 Agents Breakdown

| Agent               | Role                                    |
| ------------------- | --------------------------------------- |
| **PlannerAgent**    | Main controller, interprets user intent |
| **FlightAgent**     | Books mock flights                      |
| **HotelAgent**      | Books accommodations                    |
| **AttractionAgent** | Suggests attractions and activities     |

``
🔧 How to Run This Project
Create a .env file with your Gemini API key:

    GEMINI_API_KEY=your_key_here

    chainlit run main.py

``

✈️ Example Usage

    User: I want to go on a relaxing beach vacation in Asia.

Agent: Great! 🌴 Based on your mood, here’s a plan:
- 📍 Destination: Bali, Indonesia
- 🛫 Flight booked from Karachi to Denpasar
- 🏨 Hotel reserved at Ocean Breeze Resort
- 📸 Top Attractions: Uluwatu Temple, Kuta Beach, Balinese Spa

- 

🧠 Built With
💬 Chainlit

🧠 Gemini AI (Google)

🛠️ Python 3.10+

🙋 Created By SEERAT FATIMA 🎓 GIAIC Student | 🧠 Passionate about AI & Career Empowerment
