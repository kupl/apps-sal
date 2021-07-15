from numpy import product

def ride(group,comet):
    alph_pos = lambda l: ord(l) - 64
    compute_score = lambda name : product([ alph_pos(c) for c in name]) % 47
    group_score = compute_score(group)
    comet_score = compute_score(comet)
    return "GO" if  group_score == comet_score  else "STAY"
