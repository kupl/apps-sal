def validate_ean(code):
    return sum([int(x) if i % 2 == 0 else 3 * int(x) for i, x in enumerate(code)]) % 10 == 0
