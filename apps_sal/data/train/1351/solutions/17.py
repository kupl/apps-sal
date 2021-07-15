# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    for i in range(0,n):
        if i in lst:
            lst[i]=i 
        else:
            lst[i]=0
            
    for i in range(0,n):
        print(lst[i],end=" ")
    print()
