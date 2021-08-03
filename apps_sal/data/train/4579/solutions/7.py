def pattern(n):

    pattern = ""
    pattern_sub = ""

    for x in range(n, 0, -1):
        pattern += pattern_sub
        pattern += str(x % 10) * x
        pattern_sub += str(x % 10)
        if x > 1:
            pattern += "\n"

    return pattern
