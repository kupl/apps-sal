def winner(deck_s, deck_j):
    points = {True: ['Steve', 0], False: ['Josh', 0]}
    chek_dek = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for (s, j) in zip(deck_s, deck_j):
        point = chek_dek.index(s) - chek_dek.index(j)
        if not point:
            continue
        points[point > 0][-1] += 1
    winer = points[points[1][-1] > points[0][-1]][0]
    if points[1][-1] == points[0][-1]:
        return 'Tie'
    return f'{winer} wins {points[winer == points[1][0]][-1]} to {points[winer == points[0][0]][-1]}'
