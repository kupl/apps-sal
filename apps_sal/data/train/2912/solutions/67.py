def find_multiples(integer, limit):
    spisok = []
    for i in range(integer, limit + 1):
        if i % integer == 0:
            spisok.append(i)
    return spisok
