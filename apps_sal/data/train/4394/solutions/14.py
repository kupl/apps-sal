def men_still_standing(cards):
    A = {str(i): 0 for i in range(1, 12)}
    B = A.copy()
    for card in cards:
        if 11 - sum((1 for i in A.values() if i >= 2)) <= 6 or 11 - sum((1 for i in B.values() if i >= 2)) <= 6:
            break
        if card[-1] == 'Y':
            eval(card[0])[card[1:-1]] += 1
        elif card[-1] == 'R':
            eval(card[0])[card[1:-1]] += 2
    return (max(11 - sum((1 for i in A.values() if i >= 2)), 6), max(11 - sum((1 for i in B.values() if i >= 2)), 6))
