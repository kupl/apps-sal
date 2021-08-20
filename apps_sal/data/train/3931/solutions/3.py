from collections import Counter
reqs = {'road': Counter('bw'), 'settlement': Counter('bwsg'), 'city': Counter('ooogg'), 'development': Counter('osg')}


def build_or_buy(hand):
    return list(filter(lambda obj: not reqs[obj] - Counter(hand), reqs.keys()))
