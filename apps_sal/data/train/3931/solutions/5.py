from collections import Counter


def build_or_buy(hand):
    res = []
    bank = Counter(hand)
    if bank['b'] > 0 and bank['w'] > 0:
        res.append('road')
        if bank['s'] > 0 and bank['g'] > 0:
            res.append('settlement')
    if bank['o'] > 2 and bank['g'] > 1:
        res.append('city')
    if bank['o'] > 0 and bank['s'] > 0 and (bank['g'] > 0):
        res.append('development')
    return res
