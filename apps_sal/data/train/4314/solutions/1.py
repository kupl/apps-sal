def chess_bishop_dream(b, p, d, k): return [c - abs((q + k * e) % (2 * c) - c + .5) - .5for c, q, e in zip(b, p, d)]
