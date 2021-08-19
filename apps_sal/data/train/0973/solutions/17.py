try:
    for _ in range(int(input())):
        (n, k) = map(int, input().split())
        l = input().split()
        l = [int(i) for i in l]
        m = max(l)
        m += k
        mi = min(l)
        mi -= k
        print(m - mi)
except EOFError:
    pass
