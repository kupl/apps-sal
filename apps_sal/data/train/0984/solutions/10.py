t = int(input())
for x in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    i = 0
    count = 0
    while (i < n):
        if a[i] % 2 == 0:
            j = i + 1
            p = 0
            while (j < n):
                if a[j] % 2 != 0:
                    p += 1
                j += 1
            count += p
        i += 1
    print(count)
