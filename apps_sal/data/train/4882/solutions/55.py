def round_to_next5(n):
    cheat = [0, 1,1,1,1]
    r = int(n / 5) + (cheat [n % 5] * n > 0)
    r = r * 5
    return r
