def oddity(n):
    return ['odd', 'even'][n ** 0.5 % 1 != 0]
