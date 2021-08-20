def cake(candles, debris):
    return 'Fire!' if candles and sum((ord(c) if i % 2 == 0 else ord(c) - 96 for (i, c) in enumerate(debris))) > candles * 0.7 else 'That was close!'
