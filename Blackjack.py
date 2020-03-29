from Card import Card
from Deck import Deck
from Player import Player

action_prompt = "-----Player's Move-----\n1.Hit \n2.Stand \nEnter:"

def show_dealer_hand():
    print("-----Dealer-----")
    dealer.show()

def show_player_hand():
    print("-----{}-----".format(player.name))
    player.show()

def show_hands():
    show_dealer_hand()
    show_player_hand()

def initial_deal():
    player.draw(deck.draw())
    dealer.draw(deck.draw())
    show_dealer_hand()
    player.draw(deck.draw())
    show_player_hand()

# def is_bust():
#     hand_val = 0
#     for c in player.hand
#         hand_val = c.val
#     if(hand_val > 21)
#         return True
#     else:
#         return False

# def is_black_jack():
def new_round():
    player.discard_hand()
    dealer.discard_hand()
    print("----------New Round----------")
    initial_deal()

def black_jack_val(val):
    if(val > 10 and val < 14):
        return 10
    else:
        return val

def hand_result():
    hand_val = 0
    for c in player.hand:
        hand_val += black_jack_val(c.val)
    if(hand_val > 21):
        show_hands()
        print("{}'s hand is {}. Bust. House wins!".format(player.name, hand_val))
        new_round()
    elif(hand_val == 21):
        show_hands()
        print("{}'s hand is {}. Black Jack! {} wins!".format(player.name, hand_val, player.name))
        new_round()
    else:
        show_hands()
        print("{}'s hand is {}".format(player.name, hand_val))

#Setup card to input into deck
deck = Deck()
deck.shuffle()

dealer = Player("Dealer")
player = Player("Jack")

initial_deal()

while(True):

    #player's move
    player_move = input(action_prompt)
    #Player actions
    if(player_move == "1"):
        player.draw(deck.draw())
        hand_result()
    #Dealers actions
    elif(player_move == "2"):
        print("stand")
    else:
        print("UNRECOGNIZE COMMAND NUMBER. ENTER NUMBER IN PLAYER'S MOVE")