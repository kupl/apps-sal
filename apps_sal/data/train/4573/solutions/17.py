def over_the_road(a, n):

    if a % 2 != 0:
        return (2 * n - int(a / 2) * 2)
    else:
        return 2 * n - int(a / 2) * 2 + 1
