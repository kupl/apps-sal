def find_digit(n1, n2):
    try:
        if n2 < 0 or n2 == 0:
            return -1
        n3 = str(abs(n1))
        n4 = int('-' + str(n2))
        return int(n3[n4])
    except IndexError:
        return 0
