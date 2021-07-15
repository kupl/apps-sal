# cook your dish here
l1=int(input())
for i in range(l1):
    x=int(input())
    y=list(map(int,input().split()))
    z=list(map(int,input().split()))
    if max(z)!=max(y):
        print('YES')
    else:
        print('NO')
