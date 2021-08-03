try:
    n1 = int(input())
    for i in range(n1):
        n = list(map(int, input().split()))
        b = n[0] + n[1] - n[3]
        a = n[0] - b
        c = n[2] - a
        print(a, b, c)
except:
    pass
