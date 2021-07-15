for _ in range(int(input())):
    n,d=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l=l[::-1]
    
    for i in l:
        d=(d//i)*i
    print(d)

