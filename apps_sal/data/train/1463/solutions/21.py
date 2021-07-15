for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
        print(1,1)
        continue
    j=0
    if n%2==0:
        print(n//2)
        s=[[2,i,i+1] for i in range(1,n+1,2)]
        for i in s:
            print(*i)
    else:
        print(n//2)
        s=[[2,i,i+1] for i in range(4,n+1,2)]
        s.insert(0,[3,1,2,3])
        for i in s:
            print(*i)
