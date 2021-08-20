for _ in range(eval(input())):
    (n, k) = input().split()
    (n, k) = (int(n), int(k))
    l = [int(x) for x in input().split()]
    s1 = set(l)
    c = k
    for i in range(k):
        if 1 << i in s1:
            c -= 1
    print(max(c, 0))
