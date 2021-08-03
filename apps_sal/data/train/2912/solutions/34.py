def find_multiples(integer, limit):
    grup = []
    for i in range(1, int(limit) + 1):
        if i % integer == 0:
            grup.append(i)
    return grup
