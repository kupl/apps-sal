def combs(comb1, comb2):
    return min((next(max(i + len(c2), len(c1)) for i in range(len(c1 + c2)) if not ("*", "*") in list(zip((c1 + "." * len(c2))[i:], c2))) for c1, c2 in ((comb1, comb2), (comb2, comb1))))
