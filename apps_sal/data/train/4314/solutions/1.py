def chess_bishop_dream(b, p, d, k):
    return [c - abs((q + k * e) % (2 * c) - c + 0.5) - 0.5 for (c, q, e) in zip(b, p, d)]
