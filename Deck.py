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

    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        
deck = Deck()
deck.build()
deck.show()