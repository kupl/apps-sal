def find_unknown_number(x, y, z):
    for n in range(1, 99999999):
        if n % 3 == x and n % 5 == y and (n % 7 == z):
            return n
