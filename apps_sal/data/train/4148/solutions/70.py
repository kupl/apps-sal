def sum_digits(number):
    n = []
    for i in str(number):
        if i != '-':
            n.append(int(i))
    return sum(n)
