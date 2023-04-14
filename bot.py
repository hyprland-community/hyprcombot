import spacy
nlp = spacy.load("en_core_web_sm")

def get_name(text):
    doc = nlp(text)
    for tok in doc:
        if (tok.dep_ == "nsubj"):
            yield tok


import discord
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg: discord.Message):
    if msg.author == client.user:
        return

    doc = nlp(msg.content)
    await msg.reply(f"Doc: {doc}")
    for tok in doc:
        await msg.reply(f"{tok.dep_} :: {tok}")

with open('secret', 'r') as f:
    client.run(f.read())