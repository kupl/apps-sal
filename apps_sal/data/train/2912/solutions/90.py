def find_multiples(integer, limit):
    m = []
    for i in range(limit+1):
        if i/integer == int(i/integer):
            m.append(i)
    m.remove(0)
    return m
