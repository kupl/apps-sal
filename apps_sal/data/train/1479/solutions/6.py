import collections
T = int(input())
while T > 0:
    N = int(input())
    a = []
    for i in range(8):
        a.append(0)
    for i in range(N):
        (b, c) = [int(i) for i in input().split()]
        if b <= 8 and c > a[b - 1]:
            a[b - 1] = c
    print(sum(a))
    T -= 1
