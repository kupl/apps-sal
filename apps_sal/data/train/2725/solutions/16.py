def gimme(l):
    return [x for x in range(len(l)) if x not in [l.index(min(l)), l.index(max(l))]][0]
