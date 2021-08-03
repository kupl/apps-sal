for t in range(int(input())):
    n, l, r = map(int, input().split())
    max1 = [2**i for i in range(r)]
    if r < n:
        ls = [max1[-1]] * (n - r)
        max1.extend(ls)
    max1 = sum(max1)
    min1 = [2**i for i in range(l)]
    if l < n:
        ls = [1] * (n - l)
        min1.extend(ls)
    min1 = sum(min1)
    print(min1, max1)
