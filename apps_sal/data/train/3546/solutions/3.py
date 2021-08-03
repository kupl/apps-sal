def validate_ean(code):
    return sum(x * (i % 2 * 2 + 1) for i, x in enumerate(map(int, code))) % 10 == 0
