for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(32):
        c = 0
        for x in l:
            if x & (1 << i):
                c += 1
        if c > n // 2:
            ans |= 1 << i
    x = 0
    for i in l:
        x += i ^ ans
    print(x)
