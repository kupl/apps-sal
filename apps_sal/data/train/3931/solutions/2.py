def build_or_buy(h):
    l = {'road': 'bw', 'settlement': 'bwsg', 'city': 'ooogg', 'development': 'osg'}
    return [x for x in l if all((l[x].count(y) <= h.count(y) for y in l[x]))] if h else []
