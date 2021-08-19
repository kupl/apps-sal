def hex_digit_to_dec(s):
    if s.isdigit():
        return int(s)
    return ord(s) - ord('a') + 10


def hex_to_dec(s):
    res = 0
    max_i = len(s) - 1
    for (i, x_16) in enumerate(s):
        res += hex_digit_to_dec(x_16) * 16 ** (max_i - i)
    return res
