import random

troop_deck = {
    'Yellow':['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y10'],
    'Red':['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10'],
    'Purple':['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'],
    'Blue':['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10'],
    'Green':['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10'],
    'Orange':['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10']
    }

troop_deck_2 = []
for x in ['Y','R','P','B','G','O']:
    for y in range(1,11):
        troop_deck_2.append(str(x)+str(y))

random.shuffle(troop_deck_2)

print(troop_deck_2)
translation = {
    0 : 'Yellow',
    1 : 'Red',
    2 : 'Purple',
    3 : 'Blue',
    4 : 'Green',
    5 : 'Orange'
    }

played = [15,10,32,1,2,3,4,5,6,7,8,9,11,12,13,14,16,17,18,19,20]
played.append(25)

p1_hand = []
p2_hand = []
top_card = ""
color = ""

for x in range(0,7):
    p1_hand.append('')
    p2_hand.append('')

def new_card():
    finding = True
    while finding:
        top_card_raw = random.randint(0,60)
        if top_card_raw in played:
            print("tried & discarded {}".format(top_card_raw))
            continue
        else:
            print("found & used {}".format(top_card_raw))
            played.append(top_card_raw)
            top_card_raw = str(top_card_raw)
            finding = False

    color = translation[int(top_card_raw[0])]

    if top_card_raw[1] == 0:
        number = 10
    else:
        number = int(top_card_raw[1])

    top_card = color[0] + str(number)
    
    print(top_card)
    print(color)
    
new_card()
print(played)
