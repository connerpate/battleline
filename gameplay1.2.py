import config
import random
import win_test


def draw(player,draw_type):
    if player == "p1":
        if draw_type == "Troop":
            config.p1_hand.append(config.troop_deck[0])
        elif draw_type == "Tactic":
            config.p1_hand.append(config.tactic_deck[0])
    elif player == "p2":
        if draw_type == "Troop":
            config.p2_hand.append(config.troop_deck[0])
        elif draw_type == "Tactic":
            config.p2_hand.append(config.tactic_deck[0])
    config.played.append(config.troop_deck[0])
    del config.troop_deck[0]

def play(player,flag,played_card):
#    played_card_input = 0
#    if player == "p1":
#        played_card = config.p1_hand[played_card_input]
#    elif player == "p2":
#        played_card = config.p2_hand[played_card_input]
    draw_type = input("Draw From (Troop) or (Tactic) Deck?  ")
    draw(config.turn_indicator,draw_type)
        
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
        draw('p1','Troop')
        draw('p2','Troop')

    config.tactic_deck = [
        'Alx',
        'Dar',
        '123',
        '8-W',
        'Mud',
        'Fog',
        'Tra',
        'Des',
        'Red',
        'Sct'
        ]
    
    print()
    print()
    print("BEGIN")
    print()
    print()
    print()
    print()
    print("BOARD")
    print()
    for x in config.flag_cards:
        print("Player 1: {} --- Flag {} --- {} :Player 2".format(config.flag_cards[x]['p1'],x,config.flag_cards[x]['p2']))
    print()
    print("Remaining Troop Cards: {}".format(len(config.troop_deck)))
    print()
    print(config.troop_deck)
    print()
    print("Remaining Tactic Cards: {}".format(len(config.tactic_deck)))
    print(config.tactic_deck)
    print()
    

def turn(flag,played_card):
    play(config.turn_indicator,flag,played_card)

    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("BOARD")
    print()
    for x in config.flag_cards:
        print("Player 1: {} --- Flag {} --- {} :Player 2".format(config.flag_cards[x]['p1'],x,config.flag_cards[x]['p2']))
    print()
    print("Remaining Troop Cards: {}".format(len(config.troop_deck)))
#    print()
#    print(config.troop_deck)
    print()
    print("Remaining Tactic Cards: {}".format(len(config.tactic_deck)))
#    print(config.tactic_deck)
#    print()

    if config.turn_indicator == "p1":
        config.turn_indicator = "p2"
    else:
        config.turn_indicator = "p1"
    
    
        

    
deck_init()

print("Player 1 hand: {}".format(config.p1_hand))
#print("Player 2 hand: {}".format(config.p2_hand))
print()
flag = int(input("Flag to play on?  "))
print()
played_card = input("Card to play?  ")
print()
turn(flag,played_card)

print()
print("Player 1 hand: {}".format(config.p1_hand))
#print("Player 2 hand: {}".format(config.p2_hand))
print()

#To Do
#Get the played card to be removed from the player's hand in play(), instead of just the first card in the hand list
#Move the turn stuff into turn()
