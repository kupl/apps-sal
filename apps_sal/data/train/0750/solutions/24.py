while True:
    n = int(input())
    if n == 0:
        break
    f = 0
    a = [int(x) for x in input().split()]
    for i in range(n):
        if a[a[i] - 1] != i + 1:
            print('not ambiguous')
            f = 1
            break
    if f == 0:
        print('ambiguous')
