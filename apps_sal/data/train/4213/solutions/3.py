def array_info(x):
    TheDICT = {'len': [1, len(x)], int: [2, 0], str: [4, 0], float: [3, 0], 'void': [5, x.count(' ')]}
    for e in x:
        if e != ' ':
            TheDICT[type(e)][1] += 1
    return [[e[1] if e[1] else None] for e in sorted(TheDICT.values())] if x else 'Nothing in the array!'
