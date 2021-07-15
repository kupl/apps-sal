t=int(input())
for _ in range(t):
    l=[]
    n=int(input())
    for i in range(n+1):
        x=""
        for k in range(n-i):
            x+=" "
        for k in range(n,n-i-1,-1):
            x+=str(k)
        l.append(x)
    for i in range(len(l)-2,-1,-1):
        l.append(l[i])
    for ele in l:
        print(ele)

