def isPP(n):
    base = 2
    power = 2
    while base ** power <= n:
        while base ** power <= n:
            if base ** power == n:
                return [base, power]
            else:
                power += 1
        power = 2
        base += 1
    return None
