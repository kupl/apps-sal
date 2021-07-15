def fish(shoal):
    size, eaten = 1, 0
    for i in range(1, 10):
        if size < i:
            break
        eaten += i * shoal.count(str(i))
        size = max(size, int(((2 * eaten + 1) ** 0.5 - 1) / 2) + 1)
    return size
