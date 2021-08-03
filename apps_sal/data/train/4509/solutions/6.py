def validate_rhythm(m, score):
    t = m[0] / m[1]
    if t == 1 and m[0] not in [1, 2, 4, 8]:
        return 'Invalid rhythm'
    a = score.split('|')

    for c in score:
        if c not in '|1248':
            return 'Invalid rhythm'

    for s in a[1:-1]:
        if sum([1 / int(c) for c in s]) != t:
            return 'Invalid rhythm'

    bool = True
    for s in [a[0], a[-1]]:
        if sum([1 / int(c) for c in s]) != t:
            bool = False
    if bool:
        return 'Valid rhythm'

    if sum([1 / int(c) for c in a[0] + a[-1]]) == t:
        return 'Valid rhythm with anacrusis'

    return 'Invalid rhythm'
