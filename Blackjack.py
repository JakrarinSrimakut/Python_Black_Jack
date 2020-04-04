from Card import Card
from Deck import Deck
from Player import Player

#TODO Change 11 to Jack, 12 to Queen, 13 to King, 1 to ace
#TODO Refine stand and deal section into one method

action_prompt = "-----Player's Move-----\n1.Hit \n2.Stand \nEnter:"
new_game = True

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
    #dealer.draw(deck.draw())
    update_hand_value(player_1)
    update_hand_value(dealer)
    # TODO check dealer also for blackjack
    check_black_jack(player_1)

def new_round():
    global new_game
    player_1.discard_hand()
    dealer.discard_hand()
    print("----------New Round----------")
    new_game = True

def black_jack_val(val):
    if(val > 10 and val < 14):
        return 10
    elif(val == 1):
        return 11
    else:
        return val

def check_black_jack(player):
    if(player.hand_val == 21):
        print("{}'s hand is {}. Black Jack! {} wins!".format(player.name, player.hand_val, player.name))
        new_round()

def update_hand_value(player):
    player.hand_val = 0 #reset to not add new hand value to prev
    player.aces_in_hand = 0
    for c in player.hand:
        if(c.val == 1): #increment ace count
            player.aces_in_hand += 1
        player.hand_val += black_jack_val(c.val)
    # check if player has ace in hand and is over 21 change ace val to 1
    while(player.aces_in_hand > 0 and player.hand_val > 21):
        player.hand_val -= 10
        player.aces_in_hand -= 1

def hand_result(player, opponent):

    if(player.hand_val > 21):
        show_hands()
        print("{}'s hand is {}. Bust. {} wins!".format(player.name, player.hand_val, opponent.name))
        new_round()
    #Display 2 results for aces
    elif(player.aces_in_hand > 0):
        show_hands()
        print("{}'s hand is {} or {}".format(player.name, player.hand_val - 10, player.hand_val))
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

while(True):

    # Check if new game is needed run new game
    while(new_game):
        new_game = False
        initial_deal()

    #player's move
    player_move = input(action_prompt)
    #Player actions
    if(player_move == "1"):
        player_1.draw(deck.draw())
        update_hand_value(player_1)
        hand_result(player_1,dealer)
    #Dealers actions
    elif(player_move == "2"):
        while(dealer.hand_val < 17): #TODO Extra: if dealer has soft 17 keep playing
            dealer.draw(deck.draw())
            update_hand_value(dealer)
            hand_result(dealer,player_1)
        check_winner(player_1,dealer)
    else:
        print("UNRECOGNIZE COMMAND NUMBER. ENTER NUMBER IN PLAYER'S MOVE")