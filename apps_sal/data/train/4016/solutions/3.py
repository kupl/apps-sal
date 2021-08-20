def game(a, b, p=1):
    if p == 1 and (a == 0 or b == 0):
        return "Non-drinkers can't play"
    if a < p:
        return 'Joe'
    if b < p + 1:
        return 'Mike'
    return game(a - p, b - p - 1, p + 2)
