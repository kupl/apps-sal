from collections import Counter
PRICES = {'road': 'bw', 'settlement': 'bwsg', 'city': 'ooogg', 'development': 'osg'}


def build_or_buy(hand):
    return list(filter(lambda obj: not Counter(PRICES[obj]) - Counter(hand), PRICES.keys()))
