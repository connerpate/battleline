import config
import random
import win_test




def draw(player,draw_type):
        if draw_type == "Troop":
            config.hand[player].append(config.game_troop_deck[0])
            config.played_troop.append(config.game_troop_deck[0])
            del config.game_troop_deck[0]
        elif draw_type == "Tactic":
            config.hand[player].append(config.game_tactic_deck[0])
            config.played_tactic.append(config.game_troop_deck[0])
            del config.game_tactic_deck[0]


def play(player,flag,played_card):
        
    if player == "p1":
        flag_card_count = config.flag_cards[flag][player].count('   ')
        flag_tactic_count = config.flag_tactics[flag][player].count('   ') - 1
    else:
        flag_card_count = 3 - config.flag_cards[flag][player].count('   ')
        flag_tactic_count = 2 - config.flag_tactics[flag][player].count('   ')

    if str(played_card[-1]) == '0':
        config.flag_cards[flag][config.turn_indicator][flag_card_count] = str(played_card)
    elif str(played_card) in config.troop_deck:
        if config.turn_indicator == "p1":
            config.flag_cards[flag][config.turn_indicator][flag_card_count] = str(played_card) + str(" ")
        else:
            config.flag_cards[flag][config.turn_indicator][flag_card_count] = str(" ") + str(played_card)
    elif (played_card) in config.wildcard_tactics:
        print("Wildcard Tactic")
        config.flag_cards[flag][config.turn_indicator][flag_card_count] = str(played_card)
    elif str(played_card) in config.environment_tactics:
        print("Environment Tactic")
        config.flag_tactics[flag][config.turn_indicator][flag_tactic_count] = str(played_card)
    elif str(played_card) in config.guile_tactics:
        print("Guile Tactic")
        config.discarded.append(str(played_card))
        
    played_card_index = config.hand[player].index(played_card)
    del config.hand[player][played_card_index]

    while 1:
        draw_type = input("Draw From (Troop) or (Tactic) Deck?  ")
        if (draw_type == "Troop" or draw_type == "Tactic"):
            break
        
    draw(config.turn_indicator,draw_type)
    
    print()
       
    

def deck_init():    
    for x in ['Y','R','P','B','G','O']:
        for y in range(1,11):
            config.troop_deck.append(str(x)+str(y))
            config.game_troop_deck.append(str(x)+str(y))

    random.shuffle(config.game_troop_deck)

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

    config.game_tactic_deck = config.tactic_deck
    random.shuffle(config.game_tactic_deck)
    
    print()
    print()
    print("BEGIN")
    print()
    print()
    print()
    print()
   
    

def proceed():
    while 1:
        go_forward = input("Proceed?  Y/N  ")
        if go_forward == "Y":
            break

def readout():
    print("BOARD  --  {}".format(config.turn_indicator))
    print()
    print("P1 Tactics                       P1 Formation                                P2 Formation                      P2 Tactics")
    for x in config.flag_cards:
        print("{} :Player 1: {} --- Flag {} --- {} :Player 2: {}".format(
            config.flag_tactics[x]['p1'],
            config.flag_cards[x]['p1'],
            x,
            config.flag_cards[x]['p2'],
            config.flag_tactics[x]['p2']
            ))
    print()
    print("Remaining Troop Cards: {}".format(len(config.game_troop_deck)))
#    print(config.game_troop_deck)
#    print("Played Troop Cards: {}".format(config.played_troop))
    print()
    print("Remaining Tactic Cards: {}".format(len(config.game_tactic_deck)))
#    print(config.game_tactic_deck)
#    print("Played Tactic Cards: {}".format(config.played_tactic))
    print()
    print("Discarded Cards: {}".format(config.discarded))
    print()
    print("Cards in your hand: ")
    print(config.hand[config.turn_indicator])
    print()

def turn():
    readout()
    while 1:
        played_card = input("Card to play?  ")
        if played_card in config.hand[config.turn_indicator]:
            break  
    print()
    while 1:
        flag = input("Flag to play on?  ")
        if (flag.isnumeric() and 1 <= int(flag) <= 7):
            flag = int(flag)
            break
    
    print()
    play(config.turn_indicator,flag,played_card)
    readout()    
    print()
    proceed()        
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

    if config.turn_indicator == "p1":
        config.turn_indicator = "p2"
    else:
        config.turn_indicator = "p1"
   
        

    
deck_init()

#print("Player 1 hand: {}".format(config.hand['p1']))
#print("Player 2 hand: {}".format(config.hand['p2']))

while config.win == 0:
    turn()
#    win_test.test(config.flags,config.player,config.other_player)


#To Do
#Make Mud and Fog things
