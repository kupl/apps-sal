
def battle(player1, player2):
    l1 = []
    l2 = []
    x = min(len(player1), len(player2))
    for i in range(x):
        if player1[i][0] < player2[i][1]:
            l2.append(player2[i])
        if player2[i][0] < player1[i][1]:
            l1.append(player1[i])

    l1 += player1[x:]
    l2 += player2[x:]

    return {'player1': l1, 'player2': l2}
