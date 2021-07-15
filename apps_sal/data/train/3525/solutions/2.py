def flipping_game(a):
    current = best = 0
    for n in a:
        current = max(0, current - (n or -1))
        best = max(best, current)
    return sum(a) + (best or -1)
