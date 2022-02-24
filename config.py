# Gameplay Variables
troop_deck = []
tactic_deck = []
game_troop_deck = []
game_tactic_deck = []

wildcard_tactics = [
    'Alx',
    'Dar',
    '123',
    '8-W'
    ]

environment_tactics = [
    'Mud',
    'Fog'
    ]

guile_tactics = [
    'Tra',
    'Des',
    'Red',
    'Sct'
    ]

win=0
played_troop = []
played_tactic = []
discarded = []
turn_indicator = "p1"

flag_cards = {}
flag_tactics = {}

for x in range(1,8):
    flag_cards[x] = {'p1':['---','   ','   ','   '],'p2':['   ','   ','   ','---']}
    flag_tactics[x] = {'p1':['   ','   '],'p2':['   ','   ']}
    
flags = {
    1:[''],
    2:[''],
    3:[''],
    4:[''],
    5:[''],
    6:[''],
    7:['']
    }

# Player Variables

player = 'p1'
other_player = 'p2'

hand = {
    'p1':[],
    'p2':[]
    }
p1_hand = []
p2_hand = []

