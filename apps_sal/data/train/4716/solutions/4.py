def take_one(golds):
    if len(golds) > 1 and golds[0] >= golds[-1]:
        return golds.pop(0)
    else:
        return golds.pop() if golds else 0
        
        
def distribution_of(golds):
    golds = golds[:]
    a = b = 0
    while golds:
        a += take_one(golds)
        b += take_one(golds)
    return [a, b]
