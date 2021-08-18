def find_multiples(integer, limit):
    f = []
    for x in range(integer, limit + 1, integer):
        f.append(x)
    return f
