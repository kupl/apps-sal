def shoot(results):
    P1 = P2 = 0
    for (D, b) in results:
        P1 += D['P1'].count('X') * (b + 1)
        P2 += D['P2'].count('X') * (b + 1)
    return ('Draw!', 'Pete Wins!', 'Phil Wins!')[(P1 > P2) - (P1 < P2)]
