class PlaceAgent:
    def __init__(self, model):
        self.model = model

    def run(self, query: str) -> str:
        prompt = f"""
        You are a helpful AI travel recommender.
        Based on the user's interest: "{query}", suggest one travel destination.
        Respond like this:

        Place: <location>
        Why: <one line reason>
        """
        return self.model.generate_content(prompt).text
