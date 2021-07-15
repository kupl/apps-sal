def next_pal(val):
    int_to_digits = lambda n: [int(d) for d in str(n)]
    digits_to_int = lambda a: int("".join(map(str, a)))
    
    digits = int_to_digits(val)
    half, odd = len(digits) // 2, len(digits) % 2
    build = lambda start: digits_to_int(start + start[::-1][-half:])

    base_start = digits[:half + odd]
    possible = build(base_start)
    if possible > val:
        return possible
    return build(int_to_digits(digits_to_int(base_start) + 1))

