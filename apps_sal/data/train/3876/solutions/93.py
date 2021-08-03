def find(n):
    x = list(range(n + 1))
    y = []
    for i in x:
        if i % 3 == 0 or i % 5 == 0:
            y.append(i)
    return sum(y)
