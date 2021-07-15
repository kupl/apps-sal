# cook your dish here
t= int(input())
for _ in range(t):
    a=int(input())
    b=list(map(int,input().split()))
    s=0
    for i in b:
        if i%6!=0:
            s+=(i%6)
        else:
            s+=6
        
    print(s)
    

