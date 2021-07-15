# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in a:
        if i%2==0:
            s+=i 
            
    print(s)

