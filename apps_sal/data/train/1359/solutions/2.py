try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = [int(x) for x in input().split()]
        if n == 1:
            print(0)
            continue
        (even, odd) = (0, 0)
        for i in range(n):
            if l[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        mx = max(even, odd)
        mn = min(even, odd)
        if mn > 0:
            print(mx + (mn - 1) * 2)
        else:
            print(mx)
except EOFError:
    pass
