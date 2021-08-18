for _ in range(int(input())):
    x, n = map(int, input().split())
    reach = [0] * (x + 1)
    reach[0] = 1
    i = 1
    while i**n <= x:
        j = 1
        while j + i**n <= x:
            j += 1
        j -= 1
        while j >= 0:
            if reach[j] > 0:
                reach[j + i**n] += reach[j]
            j -= 1
        i += 1
    print(reach[-1])
