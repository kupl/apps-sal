try:
    t = int(input())
    while t:
        (a, b) = map(int, input().split())
        if a > b:
            res = b + 1
        elif a <= b:
            res = a + 1
        print(res)
        t -= 1
except:
    pass
