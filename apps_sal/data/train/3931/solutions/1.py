def build_or_buy(hand):
    d = {'bw': 'road', 'bwsg': 'settlement', 'ooogg': 'city', 'osg': 'development'}

    res = []
    for r, build in d.items():
        if all(hand.count(i) >= r.count(i) for i in set(r)):
            res.append(build)
    return res
