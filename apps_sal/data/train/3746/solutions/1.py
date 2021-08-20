def next_pal(val):

    def int_to_digits(n):
        return [int(d) for d in str(n)]

    def digits_to_int(a):
        return int(''.join(map(str, a)))
    digits = int_to_digits(val)
    (half, odd) = (len(digits) // 2, len(digits) % 2)

    def build(start):
        return digits_to_int(start + start[::-1][-half:])
    base_start = digits[:half + odd]
    possible = build(base_start)
    if possible > val:
        return possible
    return build(int_to_digits(digits_to_int(base_start) + 1))
