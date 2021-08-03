def shortest_arrang(num):
    for n in reversed(range((num + 3) // 2)):
        for j in reversed(range(n)):
            x = range(j, n + 1)
            if sum(x) == num:
                return list(reversed(x))
    return [-1]
