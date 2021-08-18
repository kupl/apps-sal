t = int(input())
for i in range(t):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    even, odd = 0, 0
    for j in range(n):
        count = (bin(a[j]).count("1"))
        if count % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

    for j in range(q):
        m = int(input())
        g = bin(m).count("1")
        a, b = even, odd
        if g % 2 == 0:
            a, b = even, odd
        else:
            a, b = odd, even
        print(a, b)
