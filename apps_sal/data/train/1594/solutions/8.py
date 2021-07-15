try:
    for i in range(int(input())):
        n=int(input())
        c=0
        for k in range(n):
            s=str(input())
            a=s.find("1")
            if(a!=k):
               c=c+1
        a=((n*(n+1))//2)
        print(a-c)
except:
    pass

