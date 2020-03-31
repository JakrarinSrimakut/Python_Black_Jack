from Card import Card
from Deck import Deck
from Player import Player

#TODO Change 11 to Jack, 12 to Queen, 13 to King, 1 to ace

action_prompt = "-----Player's Move-----\n1.Hit \n2.Stand \nEnter:"

def show_dealer_hand():
    print("-----Dealer-----")
    dealer.show()

def show_player_hand():
    print("-----{}-----".format(player_1.name))
    player_1.show()

def show_hands():
    show_dealer_hand()
    show_player_hand()

def initial_deal():
    player_1.draw(deck.draw())
    dealer.draw(deck.draw())
    show_dealer_hand()
    player_1.draw(deck.draw())
    show_player_hand()

def new_round():
    player_1.discard_hand()
    dealer.discard_hand()
    print("----------New Round----------")
    initial_deal()

def black_jack_val(val):
    if(val > 10 and val < 14):
        return 10
    else:
        return val

def update_hand_value(player):
    player.hand_val = 0 #reset to not add new hand value to prev
    for c in player.hand:
        player.hand_val += black_jack_val(c.val)

def hand_result(player, opponent):

    if(player.hand_val > 21):
        show_hands()
        print("{}'s hand is {}. Bust. {} wins!".format(player.name, player.hand_val, opponent.name))
        new_round()
    elif(player.hand_val == 21):
        show_hands()
        print("{}'s hand is {}. Black Jack! {} wins!".format(player.name, player.hand_val, player.name))
        new_round()
    else:
        show_hands()
        print("{}'s hand is {}".format(player.name, player.hand_val))

#Setup card to input into deck
deck = Deck()
deck.shuffle()

dealer = Player("Dealer")
player_1 = Player("Jack")

initial_deal()

while(True):

    #player's move
    player_move = input(action_prompt)
    #Player actions
    if(player_move == "1"):
        player_1.draw(deck.draw())
        update_hand_value(player_1)
        hand_result(player_1,dealer)
    #Dealers actions
    elif(player_move == "2"):
        while(dealer.hand_val < 17):
            dealer.draw(deck.draw())
            update_hand_value(dealer)
            hand_result(dealer,player_1)
        print("Check player's and dealer's hands")
    else:
        print("UNRECOGNIZE COMMAND NUMBER. ENTER NUMBER IN PLAYER'S MOVE")