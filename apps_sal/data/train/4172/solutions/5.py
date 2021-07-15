def solve(s, r={'((': 1, '))': 1, ')(': 2}):
    if len(s) % 2 == 1:
        return -1
    while '()' in s:
        s = s.replace('()', '')
    return sum(
        r[x]
        for x in map(''.join, zip(*[iter(s)] * 2))
    )
