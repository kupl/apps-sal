def alphabet_war(fight):
    sides = {'left': {'w': 4, 'p': 3, 'b': 2, 's': 1}, 'right': {'m': 4, 'q': 3, 'd': 2, 'z': 1}}

    left, right = ['Left', 0], ['Right', 0]

    fild = [' '] * (len(fight) + 2)

    for i, e in enumerate(' ' + fight + ' '):
        if e == '*':
            fild[i - 1:i + 2] = ['_', '_', '_']
        elif e != '*' and fild[i] != '_':
            fild[i] = e

    for e in fild:
        left[1] += sides['left'].get(e, 0)
        right[1] += sides['right'].get(e, 0)

    winer = max([left, right], key=lambda e: e[1])

    return "Let's fight again!" if left[1] == right[1] else f'{winer[0]} side wins!'
