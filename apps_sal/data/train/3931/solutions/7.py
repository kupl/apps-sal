def build_or_buy(hand):
    objects = {"road": "bw",
               "settlement": "bwsg",
               "city": "ooogg",
               "development": "osg"}
    return [key for key, val in objects.items() if not any(hand.count(c) < val.count(c) for c in set(val))]
