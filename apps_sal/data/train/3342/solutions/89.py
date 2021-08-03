def pattern(n):
    if (n < 1):
        pattern = ""
    else:
        pattern = "1"

        for i in range(2, n + 1):
            pattern = pattern + "\n" + (str(i) * i)

    return pattern
