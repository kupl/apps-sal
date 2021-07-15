def calculate_tip(a, r):
    tp = {"terrible": 0, "poor": 5, "good": 10, "great": 15, "excellent": 20}
    if tp.get(r.lower(), None) != None: return int(a*tp[r.lower()]/100 + .99)
    return 'Rating not recognised' 
