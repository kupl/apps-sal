# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    c1 = 1
    if n == 1:
        print(1, 0)
        continue
    else:
        for i in range(1, n - 1):
            t1 = sum(a[:i]) / x
            t2 = sum(a[i + 1:])
            if t1 < t2:
                c1 += 1
            elif t1 == t2:
                if i >= (n - i) - 1:
                    c1 += 1
                break
            else:
                break
        print(c1, n - c1)
