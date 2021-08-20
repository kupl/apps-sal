def buy_or_sell(pairs, fruit):

    def trade(pair):
        nonlocal fruit
        ret = ['buy', 'sell'][pair.index(fruit)]
        fruit = (set(pair) - set([fruit])).pop()
        return ret
    try:
        return [trade(pair) for pair in pairs]
    except ValueError:
        return 'ERROR'
