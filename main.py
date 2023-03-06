import random, discord,os

#RANDOM allows the bot to generate random proceedings, Discord allows the bot to communicate with Discord and OS is the operating system of the program

from discord.ext import commands
TOKEN = os.environ["token"]

intents = discord.Intents.default()
intents.message_content = True

#What the bot is going to do
bot = commands.Bot(command_prefix = "*", intents = intents)

#Random dice roll code
@bot.command(name = "roll")
async def roll(ctx,num):
  for i in range(int(num)):
    d = random.randint(1,6)
    await ctx.channel.send(f"Rolling a D6: {d}")

#Blackjack Game Code

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A' , 'J', 'Q', 'K', 'A' , 'J', 'Q', 'K', 'A' , 'J' , 'Q', 'K', 'A']

playerHand = []
dealerHand = []

#This code picks out a random card from the deck and once chosen remvoes it from the deck so there are no double ups

def dealCard(turn):
  card = random.choice(deck)
  turn.append(card)
  deck.remove(card)

#The total of the hand is calculated so the program can tell if you have more or less cards than 21, if you have over 21 you will bust

def total(turn):
  total = 0 
  face = ['J', 'K', 'Q']
  for card in turn:
    if card in range(1,11):
      total += card
    elif card in face:
      total += 10
    else: 
      if total > 11:
        total += 1
      elif:
        total += 11
  return total






#NOTHING BELLOW THIS
bot.run(TOKEN)