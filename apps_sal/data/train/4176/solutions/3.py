def cake(candles, debris):
    res = 0
    for (i, v) in enumerate(debris):
        if i % 2:
            res += ord(v) - 97
        else:
            res += ord(v)
    if res > 0.7 * candles and candles:
        return 'Fire!'
    else:
        return 'That was close!'
