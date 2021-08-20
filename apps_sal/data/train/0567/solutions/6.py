for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = 0
    for i in range(n - 2):
        l = a[i:i + 3]
        if len(set(l)) == 1:
            print('Yes')
            f = 1
            break
    if f == 0:
        print('No')
