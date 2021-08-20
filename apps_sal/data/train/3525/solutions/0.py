def flipping_game(num):
    current = 0
    biggest = 0
    for i in num:
        current = max(0, current - (i or -1))
        biggest = max(biggest, current)
    return sum(num) + (biggest or -1)
