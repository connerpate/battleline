import config


def test(flags,player,other_player):
    p1_count = 0
    p2_count = 0
    three_in_a_row = 0
    three_list = ['','','']
    flagmap = ['-','-','-','-','-','-','-','-','-']
    for x in flags:
        if flags[x][0] == 'p1':
            p1_count+=1
        elif flags[x][0] == 'p2':
            p2_count+=1

        print(three_list,three_in_a_row)
        del three_list[0]
        three_list.append(config.flags[x][0])
        

        if three_list == ['p1','p1','p1']:
            three_in_a_row = 'p1'
        if three_list == ['p2','p2','p2']:
            three_in_a_row = 'p2'

    print("Are there 3 cards in a row? - {}".format(three_list))
    print()
    print("Player 1's flag count: {}".format(p1_count))
    print("Player 2's flag count: {}".format(p2_count))
    print()
    print("Win value: {}".format(config.win))

    if three_in_a_row != 0:
        config.win = three_in_a_row

    if p1_count >= 5:
        config.win = 'p1'
    elif p1_count >= 5:
        config.win = 'p2'

    if config.win == 0:
        print("No Winner Yet...")
    elif config.win == player:
        print("You Win, {}".format(player))
    else:
        print("You Lose, {}".format(player))

    
    

    for x in flags:        
        if flags[x][0] != '':
            if flags[x][0] == player:
                flagmap[x-1] ="""


                Flag {}:
                {}
                """.format(x,player)
            else:
                flagmap[x-1] ="""
                {}
                Flag {}

                
                """.format(other_player,x)
        else:
            flagmap[x-1] ="""



            """

#    print("---{}---{}---".format(flagmap[0],flagmap[1]))
            



#config.flags[1][0] = 'p1'
#config.flags[2][0] = 'p1'
#config.flags[3][0] = 'p2'
#config.flags[4][0] = 'p1'
#config.flags[5][0] = 'p1'
#config.flags[6][0] = 'p2'
#config.flags[7][0] = 'p1'



