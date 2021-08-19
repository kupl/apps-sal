def fraction(a, b):
    if max([a, b]) % min([a, b]) == 0:
        return (a + b) // min([a, b])
    else:
        x = min([a, b]) // 2
        while True:
            if a % x == 0 and b % x == 0:
                break
            x -= 1
        return (a + b) // x
