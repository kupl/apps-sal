def winner(candidates):
    cs = [c for c in candidates if 'name' in c and 'scores' in c and (1 <= len(c['scores']) <= 2) and all((5 <= s <= 100 and s % 5 == 0 for s in c['scores']))]
    if len(cs) != 3:
        return False
    winner = False
    m = 0
    for candidate in candidates:
        s = sum(candidate['scores'])
        if 100 >= s > m:
            winner = candidate['name']
            m = s
    return winner
