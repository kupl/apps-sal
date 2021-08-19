try:
    t = int(input())
    for _ in range(t):
        c = 0
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        b = c = 0
        for i in a:
            if b < c:
                b += i
            else:
                c += i
        print(max(b, c))
except:
    pass
