def is_pronic(n):
    return n >= 0 and ((n**0.5 + 1) // 1) * (n**0.5 // 1) == n
