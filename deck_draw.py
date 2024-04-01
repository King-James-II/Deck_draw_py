import random

# Function to create a shuffled deck of cards
def create_deck():
  # Define suits and ranks
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  # Create deck by combining suits and ranks, then shuffle it
  deck = [(suit, rank)  for suit in suits for rank in ranks]
  random.shuffle(deck)
  return deck

# Function to draw a specified number of cards from the deck
def draw_card(deck, num): 
  hand = []
  # Ensure not to draw more cards than available in the deck
  if num > len(deck):
    num = len(deck)  
  # Draw cards and remove them from the deck
  for i in range(num):
    hand.append(deck.pop())
  return hand, deck

# Create a deck of cards
deck = create_deck()

# Function to display a card in ASCII art
def show_card(card):
  space = " "
  # Adjust spacing for double-digit ranks
  if len(card[1]) == 2:
    space = ""
  # Display the card using ASCII art
  print (f"""
  +-------+
  |{card[1]}     {space}|
  |       |
  |   {card[0]}   |
  |       |
  |{space}     {card[1]}|
  +-------+
  """)

# Draw cards from the deck until it is empty
while (len(deck) > 0):
  # Prompt user for the number of cards to draw
  num_cards = int(input("How many cards do you want to draw?"))
  # Draw the specified number of cards and display them
  hand, deck = draw_card(deck, num_cards)
  for card in hand:
    show_card(card)
# Inform when the deck is empty
print("We are out of cards")
