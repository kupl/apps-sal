def zeros(n):
    sums = []
    while n > 5:
        n /= 5
        sums.append(int(n))
        # print(int(n))
    a = 0
    for num in sums:
        a += int(num)
        # print(a)
    return int(a)
