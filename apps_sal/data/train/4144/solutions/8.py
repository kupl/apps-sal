def abundant(h):
    for i in range(h, 11, -1):
        temp = set([1])
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                temp.add(j)
                temp.add(i // j)
        x = sum(temp)
        if x > i:
            return [[i], [x - i]]
    return 12
