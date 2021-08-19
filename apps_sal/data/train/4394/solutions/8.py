def men_still_standing(cards):
    res = {'A': [11] + [0] * 11, 'B': [11] + [0] * 11}
    for c in cards:
        (team, num, card) = (c[0], int(c[1:-1]), c[-1])
        if res[team][num] < 2:
            res[team][num] += 1 if card == 'Y' else 2
            if res[team][num] > 1:
                res[team][0] -= 1
            if res[team][0] < 7:
                break
    return (res['A'][0], res['B'][0])
