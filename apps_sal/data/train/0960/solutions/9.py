try:
    def solve(n):
        res = ""
        while(n != 0):
            if(n % 2 == 0):
                res = "0" + res
            else:
                res = "1" + res
            n >>= 1
        return res
    t = int(input())
    for _ in range(t):
        n = int(input())
        c = 1
        for i in range(n):
            for j in range(n):
                z = solve(c)
                c += 1
                print(z, end=" ")
            print()
except EOFError:
    pass
