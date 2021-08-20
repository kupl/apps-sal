t = int(input())
for i in range(0, t):
    (n, k) = map(int, input().split())
    (a1, *a) = map(int, input().split())
    a.insert(0, a1)
    j = 0
    while j < n:
        if a[j] % k == 0:
            print(1, end='')
        else:
            print(0, end='')
        j += 1
    print('')
