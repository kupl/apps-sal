t=int(input())
for i in range(t):
    a=input()
    n,k=int(a.split()[0]),int(a.split()[1])
    s=input()
    l=list(s)
    ac=l.count('a')
    bc=l.count('b')
    u=0
    co=ac*bc*k*(k-1)//2
    for i in range(n):
        if(l[i]=='a'):
            u=u+bc
        elif(l[i]=='b'):
            bc=bc-1
    co=co+u*k
    print(co)
