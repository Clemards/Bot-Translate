import json
from googletrans import Translator
from discord.ext import commands

#Initialize
bot = commands.Bot(command_prefix="!")
f = open('config.json')
json_infos = json.load(f)
token = json_infos["BOT_TOKEN"]
f.close()


@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command(name="tips")
async def show_help(ctx):
    await ctx.channel.send("!trans [lang] [text] \n[lang] => 'en', 'fr', etc.. (Generally the two first letter of the language) \n[text] => The text you want to translate")

@bot.command(name="trans")
async def translate(ctx, lang, *word):
    sentence = ' '.join(word)
    translator = Translator()
    trans = translator.translate(sentence, dest=lang)
    await ctx.channel.send(trans.text)

bot.run(token)