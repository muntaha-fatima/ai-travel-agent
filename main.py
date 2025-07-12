

import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
import os

from agents.place_agent import PlaceAgent
from agents.planner_agent import PlannerAgent
from agents.fun_agent import FunAgent

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

place_agent = PlaceAgent(model)
planner_agent = PlannerAgent()
fun_agent = FunAgent(model)

@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hey Explorer! I'm your AI Travel Agent 🧳✨\n\nTell me what kind of adventure you dream of — be it peaceful nature or a foodie escape 🍜🌿.\n\nExample: *'I want to explore ancient cities'* or *'Beach vacation with friends'* ").send()

@cl.on_message
async def handle(message: cl.Message):
    user_input = message.content

    cl.user_session.set("query", user_input)

    if user_input.strip().lower() in ["thanks", "thank you", "shukriya"]:
        await cl.Message(content="🤗 You're most welcome, travel buddy! Need more help? Just ask!").send()
        return

    suggestion = place_agent.run(user_input)
    await cl.Message(content=f"📍 {suggestion}").send()

    
    destination = ""
    for line in suggestion.splitlines():
        if line.startswith("Place:"):
            destination = line.replace("Place:", "").strip()
            break

    cl.user_session.set("destination", destination)

    plan = planner_agent.run(destination)
    await cl.Message(content=plan).send()
    fun = fun_agent.run(destination)
    await cl.Message(content=f"🎉 Things to do in {destination}:").send()
    await cl.Message(content=fun).send()
