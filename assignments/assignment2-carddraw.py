# assignment2-carddraw.py
# program that uses an API to shuffle a deck of cards, and then draw 5
# Author Daniel Finnerty

import requests

shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
shuffle_response = requests.get(shuffle_url)
data = shuffle_response.json()

# Specify "deck_id" as the information of interest
deck_id = data["deck_id"]

# Confirm "deck id" number
print(f"Deck ID: {deck_id}\n")

# Change 'count=2' to a variable
card_qty = 5
card_pull_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={card_qty}"

card_pull_response = requests.get(card_pull_url)
data_pull = card_pull_response.json()

# Specify "cards" as the information of interest
cards = data_pull['cards']

# Print the value and suit of each card
print(f'The {card_qty} cards drawn from this deck are:')
for card in cards:
        value = card['value']
        suit = card['suit']
        print(f'{value} of {suit}')
