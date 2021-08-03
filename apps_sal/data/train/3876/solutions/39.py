def find(n):
    summe = []
    for x in range(n + 1):
        if x % 3 == 0 or x % 5 == 0:
            summe.append(x)
    return sum(summe)
