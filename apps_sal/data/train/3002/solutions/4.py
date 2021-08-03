def is_pronic(n):
    return n >= 0 and int(n**0.5) * (int(n**0.5) + 1) == n
