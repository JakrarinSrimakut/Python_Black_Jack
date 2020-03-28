class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("suit:{}, value: {}".format(self.suit, self.val))


        
