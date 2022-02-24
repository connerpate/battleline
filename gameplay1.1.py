import config
import random


def draw(player):
    if player == "p1":
        config.p1_hand.append(config.troop_deck[0])
    elif player == "p2":
        config.p2_hand.append(config.troop_deck[0])
    config.played.append(config.troop_deck[0])
    del config.troop_deck[0]

def play(player,flag):
    played_card_input = 0
    if player == "p1":
        played_card = config.p1_hand[played_card_input]
    elif player == "p2":
        played_card = config.p2_hand[played_card_input]

        
    if player == "p1":
        flag_card_count = config.flag_cards[flag]['p1'].count('   ') - 1
        if str(config.p1_hand[0])[-1] == '0':
            config.flag_cards[flag]['p1'][flag_card_count] = str(played_card)
        else:
            config.flag_cards[flag]['p1'][flag_card_count] = str(played_card) + str(" ")
        del config.p1_hand[0]
    elif player == "p2":
        flag_card_count = 3 - config.flag_cards[flag]['p2'].count('   ')
        if str(config.p2_hand[0])[-1] == '0':
            config.flag_cards[flag]['p2'][flag_card_count] = str(played_card)
        else:
            config.flag_cards[flag]['p2'][flag_card_count] = str(played_card) + str(" ")
        del config.p2_hand[0]
    

def deck_init():    
    for x in ['Y','R','P','B','G','O']:
        for y in range(1,11):
            config.troop_deck.append(str(x)+str(y))

    random.shuffle(config.troop_deck)

    for x in range(0,7):
        draw('p1')
        draw('p2')


def turn(flag):
    play(config.turn_indicator,flag)
    draw(config.turn_indicator)

    if config.turn_indicator == "p1":
        config.turn_indicator = "p2"
    else:
        config.turn_indicator = "p1"

    for x in config.flag_cards:
        print("Player 1: {} --- Flag {} --- {} :Player 2".format(config.flag_cards[x]['p1'],x,config.flag_cards[x]['p2']))
    print(config.troop_deck)
    print("Remaining Cards: {}".format(len(config.troop_deck)))
    print()
    
        

    
deck_init()
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(1)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(1)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(1)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(1)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(2)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(3)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(2)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()

turn(3)
print("Player 1 hand: {}".format(config.p1_hand))
print("Player 2 hand: {}".format(config.p2_hand))
print()



