def battle(p1, p2):
    p, p_ = p1[:], p2[:]
    for i, j in zip(p1, p2):
        if i[0] >= j[1]:
            p_.remove(j)
        if j[0] >= i[1]:
            p.remove(i)
    return {'player1': p, 'player2': p_}
