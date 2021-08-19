def divide(weight):
    c = False
    for a in range(weight):
        for b in range(a + 1):
            if a + b == weight and a % 2 == 0 and (b % 2 == 0):
                print(a, b)
                c = True
    return c
