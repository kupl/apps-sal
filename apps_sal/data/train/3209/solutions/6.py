def find_unknown_number(x, y, z):
    n = 0
    while True:
        n += 1
        a = n % 3
        b = n % 5
        c = n % 7
        if a == x and b == y and (c == z):
            return n
