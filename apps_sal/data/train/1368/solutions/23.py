# cook your dish here
t=int(input())
for _ in range(t):
    h,x=list(map(int,input().split()))
    if h>= x:
        print("Yes")
    else:
        print("No")

