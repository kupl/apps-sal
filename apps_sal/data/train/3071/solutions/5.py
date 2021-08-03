def last_digit(n1, n2):
    m1 = n1 % 10
    if m1 == 1:
        return 1
    if m1 == 2:
        if n2 == 0:
            return 1
        elif n2 % 4 == 3:
            return 8
        elif n2 % 4 == 0:
            return 6
        elif n2 % 4 == 2:
            return 4
        else:
            return 2
    if m1 == 3:
        if n2 == 0:
            return 1
        elif n2 % 4 == 0:
            return 1
        elif n2 % 2 == 0:
            return 9
        elif n2 % 4 == 3:
            return 7
        else:
            return 3
    if m1 == 4:
        if n2 == 0:
            return 1
        elif n2 % 4 == 2 or n2 % 4 == 0:
            return 6
        else:
            return 4
    if m1 == 5:
        if n2 == 0:
            return 1
        else:
            return 5
    if m1 == 6:
        if n2 == 0:
            return 1
        else:
            return 6
    if m1 == 7:
        if n2 == 0:
            return 1
        elif n2 % 4 == 3:
            return 3
        elif n2 % 4 == 0:
            return 1
        elif n2 % 4 == 2:
            return 9
        else:
            return 7
    if m1 == 8:
        if n2 == 0:
            return 1
        elif n2 % 4 == 3:
            return 2
        elif n2 % 4 == 0:
            return 6
        elif n2 % 4 == 2:
            return 4
        else:
            return 8
    if m1 == 9:
        if n2 == 0:
            return 1
        elif n2 % 2 == 1:
            return 9
        else:
            return 1
    if m1 == 0:
        if n2 == 0:
            return 1
        return 0
