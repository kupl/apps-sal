def build_or_buy(hand):
    o = {'bw': 'road', 'bwsg': 'settlement',
         'ooogg': 'city', 'osg': 'development'}
    def valid(x):
        for c in set(x):
            if hand.count(c) < x.count(c):
                return False
        return True
    return [v for k, v in o.items() if valid(k)]
