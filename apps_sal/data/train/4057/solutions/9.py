def score_hand(cards):
    summ = 0
    count_A = 0
    for symb in cards:
        if symb.isdigit():
            summ += int(symb)
        elif symb == 'A':
            count_A += 1
        else:
            summ += 10
    for i in range(count_A):
        summ += 11 * (count_A - i) if summ + 11 * (count_A - i) <= 21 else 1
    return summ
