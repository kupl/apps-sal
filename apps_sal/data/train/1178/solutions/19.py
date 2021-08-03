for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = 0
    for i in range(n):
        if c >= a[i]:
            c += 1
        else:
            break
    print(c)
