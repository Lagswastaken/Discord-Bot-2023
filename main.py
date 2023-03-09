import random, discord, os

#RANDOM allows the bot to generate random proceedings, Discord allows the bot to communicate with Discord and OS is the operating system of the program

from discord.ext import commands
TOKEN = os.environ["token"]
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#What the bot is going to do
bot = commands.Bot(command_prefix = "*", intents = intents)

#Random dice roll code
@bot.command(name = "roll")
async def roll(ctx,num):
  for i in range(int(num)):
    d = random.randint(1,6)
    await ctx.channel.send(f"Rolling a D6: {d}")

#Blackjack Game Code


async def on_ready():
    print('Logged in as {0.user}'.format(client))
@bot.command(name = "blackjack")

async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('*blackjack'):
    playerIn = True
    dealerIn = True
  
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
          else:
            total += 11
      return total
  
  #Check if the game has been won
  
    def showDealerHand():
      if len(dealerHand) == 2:
        return dealerHand[0]
      elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
  
  #Making the game run
    for _ in range(2):
      dealCard(dealerHand)
      dealCard(playerHand)
  
  #A loop that breaks once 
    while playerIn or dealerIn:
      print(f"Dealer has {showDealerHand()} and X")
      print(f"You have {playerHand} for a total of {total(playerHand)}")
      if playerIn:
        standOrHit = input("1: Stand \n2: Hit\n")
      if total(dealerHand) > 16:
        dealerIn = False
      else:
        dealCard(dealerHand)
      if standOrHit == '1':
        playerIn = False
      else:
        dealCard(playerHand)
      if total(playerHand) >= 21:
        break
      elif total(dealerHand) >= 21:
        break
  
  #Code defines all the different ways the game can be won/lost and ensures the correct winner is stated
    if total(playerHand) == 21:
      print(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      print("Blackjack! You Win!")
    elif total(dealerHand) == 21:
      print(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      print("Blackjack! Dealer wins!")
    elif total(playerHand) > 21: 
      print(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      print("You bust! Dealer wins!")
    elif total(dealerHand) > 21:
      print(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      print("Dealer busts! You win!")
    elif 21 - total(dealerHand) < 21 - total(playerHand):
      print(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      print("You both stood! The dealer was closer to 21! Dealer wins!")
    elif 21 - total(dealerHand) > 21 - total(playerHand):
      print(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      print("You both stood! You were closer to 21! You win!")
    elif 21 - total(dealerHand) == 21 - total(playerHand):
      print(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      print("You draw!")
   
  
  
#NOTHING BELLOW THIS
bot.run(TOKEN)