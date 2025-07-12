class FunAgent:
    def __init__(self, model):
        self.model = model

    def run(self, destination: str) -> str:
        prompt = f"""
        Suggest fun activities, famous dishes, and places to explore in {destination}.
        Make it vivid, fun, and use emojis!
        """
        return self.model.generate_content(prompt).text
