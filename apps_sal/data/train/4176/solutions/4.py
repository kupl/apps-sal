def cake(candles, debris):
    total = 0
    for i, x in enumerate(list(debris)):
        total += ord(x) - (96 if i % 2 == 1 else 0)
    return 'That was close!' if candles * 0.7 > total or candles == 0 else 'Fire!'
