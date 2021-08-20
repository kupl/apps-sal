def chess_bishop_dream(b, p, d, k):
    return [(lambda q, r: [r, c - r - 1][q % 2])(*divmod(q + k * e, c)) for (c, q, e) in zip(b, p, d)]
