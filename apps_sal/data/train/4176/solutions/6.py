def cake(candles, debris):
    return 'Fire!' if sum((ord(c) - (i % 2 and 96) for (i, c) in enumerate(debris))) > 0.7 * candles and candles != 0 else 'That was close!'
