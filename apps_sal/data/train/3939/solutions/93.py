def wins(hand1, hand2):
    if hand1 == 'scissors' and hand2 == 'paper':
        return '1'
    elif hand1 == 'paper' and hand2 == 'rock':
        return '1'
    elif hand1 == 'rock' and hand2 == 'scissors':
        return '1'
    else:
        return '2'


def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    else:
        return 'Player ' + wins(p1, p2) + ' won!'
