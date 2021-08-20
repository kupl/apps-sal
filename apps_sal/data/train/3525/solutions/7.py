def flipping_game(a):
    return sum(a) + max((j - i - 2 * sum(a[i:j]) for j in range(1, len(a) + 1) for i in range(j)))
