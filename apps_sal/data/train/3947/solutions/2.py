def square_digits(num):
    l = []
    for d in str(num):
        l.append(str(int(d) ** 2))
    return int(''.join(l))
