def circle_slash(n):
    return (n - (1 << n.bit_length() - 1) << 1) + 1
