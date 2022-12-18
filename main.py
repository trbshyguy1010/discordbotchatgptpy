import asyncio
import discord
from discord import app_commands
import openai

openai.api_key = "openai token here"

def generateResponse(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["Human", "AI"]
    )
    return response.choices[0].text

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
token = "your discord token here"

@tree.command(name="askme", description="ask me anything senpai uwu...", guild=discord.Object(id=1)) #guild id
async def ask(interactionlol: discord.Interaction, aske: str):
    await interactionlol.response.defer()
    response = generateResponse(aske)
    # await asyncio.sleep(20)
    await interactionlol.followup.send(response)
@tree.command(name="sync", description="sync me uwu...")
async def syncd(interactionlol: discord.Interaction):
    if interactionlol.user.id == 1 : #your user id here
        await tree.sync()
        interactionlol.response.send_message("You just got synced uwu!!")
        print("You just got synced")
    else:
        await interactionlol.response.send_message("You need to be owner to use this command")

@client.event
async def on_ready():
    print(f'{client.user} is connected')

if __name__ == '__main__':
    try:
        client.run(token)
    except Exception:
        print('Could not connect to bot: \nReasons why:\n', str(Exception))
