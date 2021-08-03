try:
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        a = int(a, 2)
        b = int(b, 2)
        res = 0
        while b > 0:
            u = a ^ b
            v = a & b
            a = u
            b = v * 2
            res += 1
        print(res)
except:
    pass
