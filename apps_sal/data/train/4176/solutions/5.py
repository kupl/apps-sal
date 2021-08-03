def cake(candles, debris):
    return "Fire!" if 10 * min(candles, (sum(map(ord, debris)) - len(debris) // 2 * 96)) > 7 * candles else "That was close!"
