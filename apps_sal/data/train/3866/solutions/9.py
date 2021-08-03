def winner(cs):
    if not (len(cs) == 3 and all('name' in c and 'scores' in c and len(c['scores']) in (1, 2) and all(5 <= s <= 100 and not s % 5 for s in c['scores']) for c in cs)):
        return False
    cs = {c['name']: (sum(c['scores']), -i) for i, c in enumerate(cs)}
    try:
        return max((c for c in cs.items() if c[1][0] <= 100), key=lambda c: c[1])[0]
    except:
        return False
