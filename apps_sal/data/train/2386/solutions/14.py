t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    li = list(map(int, input().split()))
    a = [0 for i in range(n + 1)]
    for i in li:
        if a[i] == 0:
            print(i, end=' ')
            a[i] = 1
    print()
