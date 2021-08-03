def shorter_reverse_longer(a, b):
    if len(b) > len(a):
        a, b = b, a

    return b + a[::-1] + b
