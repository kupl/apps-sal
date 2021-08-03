try:
    for _ in range(int(input())):
        a, o, g = map(int, input().split())
        res = abs(a - o)
        if(res > g):
            print(res - g)
        else:
            print(0)
except:
    pass
