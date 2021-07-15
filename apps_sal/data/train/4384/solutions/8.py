def fraction(a, b):
    # check if one arguments can serve as the denominator
    if max([a, b]) % min([a, b]) == 0:
        return (a + b) // min([a, b])
    # otherwise start from the half of the smallest argument and search it
    else:
        x = min([a, b]) // 2
        while True:
            if a % x == 0 and b % x == 0:
                break
            x -= 1
        return (a + b) // x
