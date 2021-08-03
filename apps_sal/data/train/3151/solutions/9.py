def totalAmountVisible(n, sides):
    return sides * (1 + sides) // 2 - (sides + 1 - n)
