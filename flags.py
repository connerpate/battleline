import config

class flag:

    def __init__(self,number):
        self.number = number
        self.won = 0
        self.formation = {
            'p1' : [],
            'p2' : []
            }
        self.p1_tactics = []
        self.p2_tactics = []

        print("Flag {} initialized!".format(self.number))
        print("Win Value: {}".format(self.won))

    def draw(self,player,turn_indicator,draw_type):
        if draw_type == "Troop":
            self.formation[turn_indicator].append(config.troop_deck[0])
            config.played_troop.append(config.troop_deck[0])
            del config.troop_deck[0]
        elif draw_type == "Tactic":
            self.formation[turn_indicator].append(config.tactic_deck[0])
            config.played_tactic.append(config.troop_deck[0])
            del config.tactic_deck[0]
        
    def flag_win_test(self,turn_indicator):
        if len(self.formation[turn_indicator])== 3:
            if input("Claim flag? : Y/N  ") == "Y":
                self.won = 1
        print("Win Indicator for {}: {}".format(turn_indicator,self.won))
        print("Current formation: {}".format(self.formation[turn_indicator]))

    def add_card(self,turn_indicator,played_card):
        self.formation[turn_indicator].append(played_card)
        
flag_1 = flag(1)

flag_1.add_card("p1","R1")
flag_1.flag_win_test("p1")

flag_1.add_card("p2","R3")
flag_1.flag_win_test("p2")

flag_1.add_card("p1","R2")
flag_1.flag_win_test("p1")

flag_1.add_card("p1","R5")
flag_1.flag_win_test("p1")
