def solve(a, b):
    Alice = 0
    Bob = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            Alice += 1
        elif a[i] < b[i]:
            Bob += 1
    if Alice > Bob:
        return '{0}, {1}: Alice made "Kurt" proud!'.format(Alice, Bob)
    elif Alice < Bob:
        return '{0}, {1}: Bob made "Jeff" proud!'.format(Alice, Bob)
    else:
        return '{0}, {1}: that looks like a "draw"! Rock on!'.format(Alice, Bob)
