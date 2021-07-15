a=int(input())
for i in range(0,a):
    b=int(input())
    c=list(map(int,input().split()))
    if(c[0]>c[len(c)-1]):
        print(c[0])
    else:
        print(c[len(c)-1])
