def score_test(t, r, o, w):
    
    return sum([r,o,-w][s]for s in t)
