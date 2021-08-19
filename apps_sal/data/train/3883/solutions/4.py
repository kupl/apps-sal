def solve(stg):
    split = [[], []]
    for c in sorted(stg):
        split[0 if c in 'aeiou' else 1].append(c)
    (a, b) = sorted(split, key=len, reverse=True)
    if len(a) - len(b) > 1:
        return 'failed'
    return ''.join((f'{c}{d}' for (c, d) in zip(a, b + [''])))
