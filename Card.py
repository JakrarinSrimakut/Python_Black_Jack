class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    #show card
    def show(self):
        print("{} of {}".format(self.val, self.suit))