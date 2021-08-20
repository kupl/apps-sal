t = int(input())
for i in range(t):
    (a1, a2, a3, a4, a5, p) = list(map(int, input().split()))
    c = a1 * p + a2 * p + a3 * p + a4 * p + a5 * p
    if c <= 120:
        print('No')
    else:
        print('Yes')
