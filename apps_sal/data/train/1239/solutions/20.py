for i in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n+1):
        s=""
        for j in range(i+1):
            s+=str(n-j)
        s=" "*(n-i)+s
        a.append(s)
    print(*a,sep='\n')
    a.reverse()
    print(*a[1:],sep='\n')

