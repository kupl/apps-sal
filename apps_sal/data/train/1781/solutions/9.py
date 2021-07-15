SPECIAL = {"J": 1,
           "Q": 2,
           "K": 3,
           "A": 4}

def who_wins_beggar_thy_neighbour(hand_1, hand_2):
    turn = 0
    players = [[SPECIAL.get(card[0], 0) for card in hand] for hand in (hand_1, hand_2)]
    pot = []
    penalty = 0
    time = 0
    
    while time < 10000:
        time += 1
        try:
            if penalty:
                for __ in range(penalty):
                    card = players[turn].pop(0)
                    pot.append(card)
                    if card:
                        break
                else:
                    players[(turn+1) % 2] += pot
                    pot = []
            else:
                card = players[turn].pop(0)
                pot.append(card)
        except IndexError:
            return (turn+1) % 2
        
        penalty = card
        turn = (turn+1) % 2

