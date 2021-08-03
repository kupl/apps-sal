def animals(heads, legs):
    a, b = 2 * heads - legs / 2, legs / 2 - heads

    if a < 0 or b < 0 or [a % 1, b % 1] != [0, 0]:
        return 'No solutions'
    else:
        return (a, b)
