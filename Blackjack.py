from Card import Card
from Deck import Deck
from Player import Player

action_prompt = "1.Hit \n2.Stand"

def initial_deal():
    player.draw(deck.draw())
    dealer.draw(deck.draw())
    print("Dealer:  ")
    dealer.show()
    player.draw(deck.draw())
    print("{}:  ".format(player.name))
    player.show()

#Setup card to input into deck
deck = Deck()
deck.shuffle()

dealer = Player("Dealer")
player = Player("Jack")

while(True):
    initial_deal()

    player.show()
    #player's move
    player_move = input(action_prompt)
