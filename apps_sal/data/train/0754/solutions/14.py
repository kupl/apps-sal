try:
    def check(n):
        while(n!=0):
            if (n%10)%2==0:
                return 1
            n//=10
        return 0
    t=int(input())
    for _ in range(t):
        n=int(input())
        print(check(n))
except EOFError:
    pass
