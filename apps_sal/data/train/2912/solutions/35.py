def find_multiples(integer, limit):
    divizor = []
    for i in range(limit + 1):
        if i < integer:
            pass
        elif i % integer == 0:
            divizor.append(i)
    return divizor
