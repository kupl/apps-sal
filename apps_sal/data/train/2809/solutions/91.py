def digitize(n):
    len_n = str(n)
    list = []
    for i in range(0, len(len_n)):

        a = n % 10
        n = n // 10

        list.append(a)

    return list
