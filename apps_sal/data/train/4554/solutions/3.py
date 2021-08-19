def play_if_enough(hand, play):
    a = dict([(x, hand.count(x)) for x in set(hand)])
    b = dict([(x, play.count(x)) for x in set(play)])
    if not False in [a.get(i, 0) > b.get(i, 0) for i in a] and hand != '':
        return (True, ''.join([str(x * (a[x] - b.get(x, 0))) for x in a]))
    return (False, hand)
