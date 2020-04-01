from Card import Card
from Deck import Deck
from Player import Player

#TODO Check on initial_deal() for black jack
#TODO Change 11 to Jack, 12 to Queen, 13 to King, 1 to ace
#TODO Refine stand and deal section into one method

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

def check_black_jack(player):
        if(player.hand_val == 21):
            print("{}'s hand is {}. Black Jack! {} wins!".format(player.name, player.hand_val, player.name))
            #TODO return True or False to restart game 

def initial_deal():
    dealer.draw(deck.draw())
    player_1.draw(deck.draw())
    show_dealer_hand()
    player_1.draw(deck.draw())
    show_player_hand()
    update_hand_value(player_1)
    update_hand_value(dealer)
    check_black_jack(player_1)

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
    # set indicator for ace
    for c in player.hand:
        #TODO Give value of ace as 1 or 11
        player.hand_val += black_jack_val(c.val)
    # check if player has ace in hand and is over 21 change ace val to 1
    
def hand_result(player, opponent):

    if(player.hand_val > 21):
        show_hands()
        print("{}'s hand is {}. Bust. {} wins!".format(player.name, player.hand_val, opponent.name))
        new_round()

    else:
        show_hands()
        print("{}'s hand is {}".format(player.name, player.hand_val))


def check_winner(player, opponent):
    if(player.hand_val > opponent.hand_val):
        print("{} wins!".format(player.name))
    elif(player.hand_val < opponent.hand_val):
        print("{} wins!".format(opponent.name))
    else:
        print('Tie!')
    new_round()
    
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
        check_winner(player_1,dealer)
    else:
        print("UNRECOGNIZE COMMAND NUMBER. ENTER NUMBER IN PLAYER'S MOVE")