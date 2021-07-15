try:
    for z in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        z=max(a)
        b=[]
        for i in range(z):
            b.append(a.count(i+1))
        print(min(b))
except:
    pass
