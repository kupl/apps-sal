def find_squares(x, y):
    return sum(((x - k) * (y - k) for k in range(min(x, y))))


findSquares = find_squares
