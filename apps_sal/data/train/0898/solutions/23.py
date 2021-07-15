try:
    def find(x,y):
        p=x+y+(x*y)
        s1=str(x)
        s2=str(y)
        s3=str(p)
        return (s3==(s1+s2))
    for _ in range(int(input())):
        m,n=map(int,input().split())
        n+=1
        l=len(str(n))-1
        if(l==0):
            print("0 0")
        else:
            print((l*m),m)
except EOFError as e:
    pass
