def score_hand(cards):
    total = 0
    Ace = 0
    for str in cards:
        if str == '1':
            total += 1
        if str == '2':
            total += 2
        if str == '3':
            total += 3
        if str == '4':
            total += 4
        if str == '5':
            total += 5
        if str == '6':
            total += 6
        if str == '7':
            total += 7
        if str == '8':
            total += 8
        if str == '9':
            total += 9
        if str == '10' or str == 'J' or str == 'Q' or (str == 'K'):
            total += 10
        if str == 'A':
            Ace += 1
    if Ace == 1:
        if total < 11:
            total += 11
        else:
            total += 1
    if Ace > 1:
        for i in range(Ace):
            if total < 10:
                total += 11
            else:
                total += 1
    return total
