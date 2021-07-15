special={'J':1,'Q':2,'K':3,'A':4}
def who_wins_beggar_thy_neighbour(hand_1, hand_2):
    h=[hand_1[:],hand_2[:]]
    pile=[]
    turn=0
    for _ in range(10000):
        while(not pile or pile[-1][0] not in special):
            if not h[turn]:
                return turn^1
            pile.append(h[turn].pop(0))
            turn^=1
        count=special[pile[-1][0]]
        while(count>0):
            if not h[turn]:
                return turn^1
            pile.append(h[turn].pop(0))
            if pile[-1][0] in special:
                count=special[pile[-1][0]]
                turn^=1
                continue
            count-=1
        turn^=1
        h[turn]+=pile
        pile=[]            
    return None
