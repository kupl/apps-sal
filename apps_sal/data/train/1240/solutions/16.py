n = int(input())
for _ in range(n):
    k = int(input())
    a = [int(i) for i in input().split()]
    sum = 0
    for i in range(k):
        if a[i] % 6 == 0:
            sum += 6
            continue
        a[i] = a[i] % 6
        sum += a[i]
    print(sum)
