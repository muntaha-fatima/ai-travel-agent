from tools.travel_tools import get_flights
from tools.hotel_tool import suggest_hotels

class PlannerAgent:
    def run(self, destination: str) -> str:
        flights = get_flights(destination)
        hotels = suggest_hotels(destination)

        plan = f"✈️ Travel Options to {destination}:" + "\n".join(flights)
        plan += f"\n\n🏨 Stay Options in {destination}:" + "\n".join(hotels)
        return plan
