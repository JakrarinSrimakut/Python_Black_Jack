import random
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    #Build deck of cards    
    def build(self):
        for s in ["Spades", "Clubs", "Hearts", "Dimonds"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    #Show cards in deck
    def show(self):
        for c in self.cards:
            c.show()
    
    #Shuffle order of cards
    def shuffle(self):
        random.shuffle(self.cards)

    #Draw top card
    def draw(self):
        return self.cards.pop()