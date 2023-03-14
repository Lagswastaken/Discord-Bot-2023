import random, discord, os, math, asyncio



#RANDOM allows the bot to generate random proceedings, Discord allows the bot to communicate with Discord and OS is the operating system of the program

from discord.ext import commands
TOKEN = os.environ["token"]

intents = discord.Intents.default()
intents.message_content = True

#What the bot is going to do
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix = "*", intents = intents)

#Random dice roll code
@bot.command(name = "roll")
async def roll(ctx,num):
  for i in range(int(num)):
    d = random.randint(1,6)
    await ctx.channel.send(f"Rolling a D6: {d}")

#Paper Scissors Rock
@bot.command(name='psr')
async def psr(ctx):
  computer_choice = ''
  await ctx.channel.send("Lets play Paper, Scissors, Rock!")
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  player_choice = ''
  userPlaying = True
  await ctx.channel.send("What do you choose?")
  if userPlaying:
    response = await bot.wait_for("message")
  if response.content == 'paper':
     player_choice = 'paper'
    
  elif response.content == 'rock':
     player_choice = 'rock'

  elif response.content == 'scissors':
     player_choice = 'scissors'

  if player_choice == computer_choice:
        result = "It's a tie!"
  elif player_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
  elif player_choice == "paper" and computer_choice == "rock":
        result = "You win!"
  elif player_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
  else:
        result = "Computer wins."

        await ctx.channel.send(f"You chose {player_choice}, and the computer chose {computer_choice}. {result}")

  
   
  

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



@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@bot.command(name = 'blackjack')
async def blackjack(ctx):
        playerHand.clear()
        dealerHand.clear()
        for _ in range(2):
          dealCard(dealerHand)
          dealCard(playerHand)
        playerIn = True
        dealerIn = True
        await ctx.channel.send("Welcome to blackjack!")
        while playerIn or dealerIn:
           await ctx.channel.send(f"Dealer has {showDealerHand()} and X")
           await ctx.channel.send(f"You have {playerHand} for a total of {total(playerHand)}")
           if playerIn:
                response = await bot.wait_for("message")
           if response.content == 'stand':
                    playerIn = False
           elif response.content == 'hit':
                    dealCard(playerHand)
           if total(playerHand) >= 21:
                        playerIn = False
           if total(dealerHand) > 16:
                dealerIn = False
           else:
                dealCard(dealerHand)
           if total(dealerHand) >= 21:
                dealerIn = False
           if total(playerHand) >= 21:
                playerIn = False
          
          #Code defines all the different ways the game can be won/lost and ensures the correct winner is stated
           if total(playerHand) == 21:
            await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
            await ctx.channel.send("Blackjack! You Win!")
            break
           elif total(dealerHand) == 21:
            await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
            await ctx.channel.send("Blackjack! Dealer wins!")
            break
           elif total(playerHand) > 21: 
            await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
            await ctx.channel.send("You bust! Dealer wins!")
            break
           elif total(dealerHand) > 21:
            await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
            await ctx.channel.send("Dealer busts! You win!")
            break
           elif 21 - total(dealerHand) < 21 - total(playerHand):
            await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
            await ctx.channel.send("You both stood! The dealer was closer to 21! Dealer wins!")
            break
           elif 21 - total(dealerHand) > 21 - total(playerHand):
            await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
            await ctx.channel.send("You both stood! You were closer to 21! You win!")
            break
           elif 21 - total(dealerHand) == 21 - total(playerHand):
            await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
            await ctx.channel.send("You Draw! No one wins!")
            break
         
      


#NOTHING BELLOW THIS
bot.run(TOKEN)

