# Importing necessary libraries and modules
import random, discord, os, math, asyncio
from discord.ext import commands

# Storing the token as an environment variable for security purposes
TOKEN = os.environ["token"]

# Creating a Discord client and bot instance with default intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix = "*", intents = intents)

# Command to roll a D6 dice
@bot.command(name = "roll")
async def roll(ctx,num):
  for i in range(int(num)):
    # Rolling a D6 dice and sending the result to the channel
    d = random.randint(1,6)
    await ctx.channel.send(f"Rolling a D6: {d}")

# Command to play Paper Scissors Rock game
@bot.command(name='psr')
async def psr(ctx):
  # Sending a message to the channel to start the game
  await ctx.channel.send("Let's play Paper, Scissors, Rock!")
  
  # Defining the choices for the game
  choices = ["rock", "paper", "scissors"]
  # Randomly selecting the computer's choice
  computer_choice = random.choice(choices)
  
  # Initializing the game with user playing
  userPlaying = True
  
  # Asking user for their choice
  await ctx.channel.send("What do you choose?")
  
  # Waiting for the user to respond with their choice
  if userPlaying:
    response = await bot.wait_for("message")
  
  # Assigning the choice to the player
  if response.content == 'paper':
     player_choice = 'paper'  
  elif response.content == 'rock':
     player_choice = 'rock'
  elif response.content == 'scissors':
     player_choice = 'scissors'
     
  # Checking the result of the game
  if player_choice == computer_choice:
        result = "It's a tie!"
        await ctx.channel.send(f"You chose {player_choice}, and the computer chose {computer_choice}. {result}")
  elif player_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
        await ctx.channel.send(f"You chose {player_choice}, and the computer chose {computer_choice}. {result}")
  elif player_choice == "paper" and computer_choice == "rock":
        result = "You win!"
        await ctx.channel.send(f"You chose {player_choice}, and the computer chose {computer_choice}. {result}")
  elif player_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
        await ctx.channel.send(f"You chose {player_choice}, and the computer chose {computer_choice}. {result}")
  else:
        result = "Computer wins."
        await ctx.channel.send(f"You chose {player_choice}, and the computer chose {computer_choice}. {result}")

# Defining a deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A' , 'J', 'Q', 'K', 'A' , 'J', 'Q', 'K', 'A' , 'J' , 'Q']


# Initialize empty playerHand and dealerHand lists
playerHand = []
dealerHand = []

# Function to deal a card from the deck
def dealCard(turn):
  card = random.choice(deck) # pick a random card from deck
  turn.append(card) # add the card to the turn (player or dealer)
  deck.remove(card) # remove the card from the deck

# Function to calculate the total value of a player's hand
def total(turn):
  total = 0 
  face = ['J', 'K', 'Q'] # face cards have a value of 10
  for card in turn:
    if card in range(1,11): # numeric cards have their face value
      total += card
    elif card in face: # face cards have a value of 10
      total += 10
    else: # Ace has value of 1 or 11 depending on total
      if total > 11:
        total += 1
      else:
        total += 11
  return total

# Function to show the dealer's hand, hiding the second card
def showDealerHand():
  if len(dealerHand) == 2:
    return dealerHand[0]
  elif len(dealerHand) > 2:
    return dealerHand[0], dealerHand[1]

# Discord bot event to handle blackjack command
@bot.command(name = 'blackjack')
async def blackjack(ctx):
  playerHand.clear() # empty playerHand list
  dealerHand.clear() # empty dealerHand list
  for _ in range(2):
    dealCard(dealerHand) # deal 2 cards to the dealer
    dealCard(playerHand) # deal 2 cards to the player
  playerIn = True
  dealerIn = True
  await ctx.channel.send("Welcome to blackjack!")
  while playerIn or dealerIn:
    await ctx.channel.send(f"Dealer has {showDealerHand()} and X")
    await ctx.channel.send(f"You have {playerHand} for a total of {total(playerHand)}")
    if playerIn:
      response = await bot.wait_for("message")
      if response.content == 'stand':
        playerIn = False # player chooses to stand
      elif response.content == 'hit':
        dealCard(playerHand) # player chooses to hit
    else:
      dealCard(dealerHand) # dealer takes a turn
    # Check if dealer's total hand value is greater than or equal to 21
    if total(dealerHand) >= 21:
      dealerIn = False
    
    # Check if player's total hand value is greater than or equal to 21
    if total(playerHand) >= 21:
      playerIn = False
    
    # Check if player has a blackjack
    if total(playerHand) == 21:
      await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      await ctx.channel.send("Blackjack! You Win!")
      break
    
    # Check if dealer has a blackjack
    elif total(dealerHand) == 21:
      await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      await ctx.channel.send("Blackjack! Dealer wins!")
      break
    
    # Check if player has busted (total hand value greater than 21)
    elif total(playerHand) > 21: 
      await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      await ctx.channel.send("You bust! Dealer wins!")
      break
    
    # Check if dealer has busted (total hand value greater than 21)
    elif total(dealerHand) > 21:
      await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      await ctx.channel.send("Dealer busts! You win!")
      break
    
    # Check if dealer's total hand value is closer to 21 than player's
    elif 21 - total(dealerHand) < 21 - total(playerHand):
      await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      await ctx.channel.send("You both stood! The dealer was closer to 21! Dealer wins!")
      break
    
    # Check if player's total hand value is closer to 21 than dealer's
    elif 21 - total(dealerHand) > 21 - total(playerHand):
      await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      await ctx.channel.send("You both stood! You were closer to 21! You win!")
      break
    
    # Check if player's and dealer's total hand values are equal
    elif 21 - total(dealerHand) == 21 - total(playerHand):
      await ctx.channel.send(f"\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
      await ctx.channel.send("You Draw! No one wins!")
      break
    
      


#NOTHING BELLOW THIS
bot.run(TOKEN)

