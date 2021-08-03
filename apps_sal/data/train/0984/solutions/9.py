t = int(input())
for x in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    i = 0
    count = 0
    j = 0
    while (j < n):
        if a[j] % 2 == 0:
            i += 1
        else:
            count += i
        j += 1
    print(count)
