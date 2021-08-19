t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split()))
    n = 1
    m = 2
    k = 0
    l = 0
    while n <= a:
        k += 1
        a -= n
        n += 2
    while m <= b:
        l += 1
        b -= m
        m += 2
    if k == l:
        print('Bob')
    elif k < l:
        print('Bob')
    elif k > l:
        print('Limak')
