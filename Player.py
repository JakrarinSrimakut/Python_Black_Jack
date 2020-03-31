from Card import Card
from Deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_val = 0

    #Draw card append to hand
    def draw(self, card):
        self.hand.append(card)

    #Show hand
    def show(self):
        i = 1
        for c in self.hand:
            print("{}.".format(i), end = " ")
            c.show()
            i += 1

    def discard_hand(self):
        self.hand.clear()

    #Discard card hand with number
    def discard_specific_card(self, card_number):
        if ( 0 <= card_number -1 and card_number-1 < len(self.hand)):
            del self.hand[card_number-1]
        else:
            print("Unidentifiable number")