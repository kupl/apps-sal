try:
    def solve(n):
        res=""
        for i in range(n):
            if i%2==0:
                res+="1"
            else:
                res+="0"
        return res
    t=int(input())
    for _ in range(t):
        n = int(input())
        z=solve(n)
        for i in range(n):
            print(z)
       
except EOFError:
    pass
