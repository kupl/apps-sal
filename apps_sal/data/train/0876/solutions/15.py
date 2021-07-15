# cook your dish here
t=int(input())
for i in range(0,t):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    if((max(a)-min(a))<k):
        print("YES")
    else:
        print("NO")
        

