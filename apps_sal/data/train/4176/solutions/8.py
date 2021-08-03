def cake(candles, debris):
    a = ord('a') - 1
    res = sum(ord(x) if i % 2 == 0 else (ord(x) - a) for i, x in enumerate(debris))
    return 'That was close!' if candles == 0 or res / candles <= 0.7 else 'Fire!'
