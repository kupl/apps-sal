from collections import Counter


def naughty_or_nice(data):
    c = Counter(x for v in data.values() for x in v.values())
    return 'Nice!' if c['Nice'] >= c['Naughty'] else 'Naughty!'
