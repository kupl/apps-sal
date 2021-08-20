def find_multiples(integer, limit):
    i = 1
    y = []
    while integer * i <= limit:
        output = integer * i
        y.append(output)
        i += 1
    return y
