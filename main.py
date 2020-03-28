from Card import Card
from Deck import Deck
from Player import Player

#Setup card to input into deck
deck = Deck()
deck.shuffle()

jack = Player("Jack")
jack.draw(deck.draw())
jack.draw(deck.draw())
jack.draw(deck.draw())
jack.show()
jack.discard(0)
print("---------------------")
jack.show()
print("---------------------")
jack.discard(4)
jack.show()