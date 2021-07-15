# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=l.index(1)
    print(x)

