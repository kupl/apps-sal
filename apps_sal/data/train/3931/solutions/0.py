from collections import Counter

REQUIRE = {x: Counter(s) for x, s in [('road', 'bw'), ('settlement', 'bwsg'), ('city', 'ooogg'), ('development', 'osg')]}


def build_or_buy(hand):
    h = Counter(hand)
    return [item for item, c in REQUIRE.items() if not c - h]
