def winner(candidates):
    if any(c.keys() != ['name', 'scores'] for c in candidates):
        return False
    if any([len(candidates)!= 3, 
            any(len(c['scores']) not in (1,2) for c in candidates),
            any( not(5 <= i <= 100) or (i % 5 != 0) for c in candidates for i in c['scores'])]):
        return False

    m = 0
    for c in candidates:
        if m < sum(c['scores']) <= 100:
            m = sum(c['scores'])
            w = c['name']
    return w if m > 0 else False
