for _ in range(int(input())):
    a=input()
    l=list(map(int,input().split()))
    q=int(input())
    r=[]
    for i in range(q):
        a,b=list(map(int,input().split()))
        print(sum(l[a-1:b]))
    
    

