def find_multiples(integer, limit):
    mas = []
    n = integer
    while n <= limit:
        mas.append(n)
        n += integer
    return mas
