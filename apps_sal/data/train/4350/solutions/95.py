def pre_fizz(n):
    a = []
    if n == 1:
        return [1]
    for i in range(1, n + 1):
        a.append(i)

    return a
