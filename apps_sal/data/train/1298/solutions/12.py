for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n + 1):
        if a[i] > a[0]:
            break
    if a[0] == a[n]:
        print(0)
    else:
        print(n - i + 1)
