t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    j = -1
    x = 0
    y = 0
    while i < n:
        if a[i] != 0:
            x = i
            break
        else:
            i += 1
    while j > -n:
        if a[j] != 0:
            y = n + j
            break
        else:
            j -= 1
    print(y - x + 1)
