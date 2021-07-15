def winner(candidates):
    if len(candidates) != 3 or not all(set(('name','scores'))==set(c.keys()) and len(c['scores']) in [1, 2] and all(s%5==0 and s>=5 and s<=100 for s in c['scores']) for c in candidates):
        return False
    candidates = filter(lambda c:sum(c['scores']) <= 100, candidates)
    return sorted(candidates, key=lambda c:-sum(c['scores']))[0]['name'] if candidates else False
