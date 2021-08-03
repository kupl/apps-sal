for _ in range(int(input())):
    x, y, n = list(map(int, input().split()))
    z = []
    count = 0
    for i in range(n + 1):
        z.append(i)
    for j in range(len(z)):
        if((x ^ z[j]) < (y ^ z[j])):
            count += 1
    print(count)
