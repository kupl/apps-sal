def digitize(n):
    list = []
    while n > 0:
        list.append(int(n % 10))
        n = int(n / 10)
    return list
