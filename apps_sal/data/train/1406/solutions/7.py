for _ in range(int(input())):
    (n, q) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in range(n):
        c = bin(a[i]).count('1')
        if c % 2 == 0:
            even += 1
        else:
            odd += 1
    for i in range(q):
        p = int(input())
        c = bin(p).count('1')
        (e, o) = (even, odd)
        if c % 2 == 0:
            (e, o) = (even, odd)
        else:
            (e, o) = (odd, even)
        print(e, o)
