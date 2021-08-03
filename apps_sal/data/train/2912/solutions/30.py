def find_multiples(integer, limit):
    out = []
    for i in range(integer, limit + 1, integer):
        out.append(i)
    return out
