def game(a, b):
    if a == 0 or b == 0:
        return "Non-drinkers can't play"
    i, n, x = 0, 1, [a, b]
    while x[i] >= n:
        x[i] -= n
        n += 1
        i ^= 1
    return 'Joe' if i == 0 else 'Mike'
