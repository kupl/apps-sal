def cake(candles, debris):
    s = sum((ord(c) if i % 2 == 0 else ord(c) - 96 for (i, c) in enumerate(debris)))
    return 'Fire!' if s > 0.7 * candles and candles > 0 else 'That was close!'
