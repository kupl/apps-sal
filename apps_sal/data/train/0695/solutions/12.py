for t in range(int(input())):
    x, y, n = list(map(int, input().split()))
    count = 0
    for i in range(n + 1):
        if (x ^ i) < (y ^ i):
            count += 1
    print(count)
