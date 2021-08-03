try:
    def solve(n):
        res = ""
        for i in range(n):
            if i % 2 == 0:
                res += "0"
            else:
                res += "1"
        return res
    t = int(input())
    for _ in range(t):
        n = int(input())
        z1 = solve(n)
        z2 = ""
        for i in z1:
            if i == "0":
                z2 += "1"
            else:
                z2 += "0"
        for i in range(n):
            if(i % 2 == 0):
                print(z1)
            else:
                print(z2)
except EOFError:
    pass
