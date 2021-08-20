def buy_or_sell(pairs, fruit):
    res = []
    for (b, s) in pairs:
        if fruit == b:
            fruit = s
            res.append('buy')
        elif fruit == s:
            fruit = b
            res.append('sell')
        else:
            return 'ERROR'
    return res
