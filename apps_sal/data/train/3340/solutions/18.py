def sharkovsky(a, b):
    a_red = a
    a_rem = a % 2
    a_count = 0
    while a_rem == 0:
        a_count = a_count + 1
        a_red = int(a_red / 2)
        a_rem = a_red % 2
    b_red = b
    b_rem = b % 2
    b_count = 0
    while b_rem == 0:
        b_count = b_count + 1
        b_red = int(b_red / 2)
        b_rem = b_red % 2
    if a_red > 1 and b_red > 1:
        if a_count != b_count:
            return a_count < b_count
        else:
            return a_red < b_red
    elif a_red == 1 and b_red > 1:
        return False
    elif a_red > 1 and b_red == 1:
        return True
    else:
        return a_count > b_count
