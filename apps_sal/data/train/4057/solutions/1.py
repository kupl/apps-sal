def score_hand(cards):
    total = 0
    number_of_aces = 0
    for i in cards:
        if i == 'A':
            total += 1
            number_of_aces += 1
        elif i == 'J' or i == 'Q' or i == 'K':
            total += 10
        else:
            total += int(i)
    if total <= 11 and number_of_aces >= 1:
        total += 10
    return total
