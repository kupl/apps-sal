# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    l=[]
    if n%2==0:
        for i in range(1,n+1,2):
            print(i+1,end=' ')
            print(i,end=' ')
        print()
    else:
        for i in range(1,n-2,2):
            print(i+1,end=' ')
            print(i,end=' ')
        print(n-1,n,n-2)
