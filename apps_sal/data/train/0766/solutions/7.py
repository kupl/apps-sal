# cook your dish here
t= int(input())
for _ in range(t):
    a=int(input())
    b=list(map(int,input().split()))
    b.sort()
    print(b[-1]*b[-2],b[0]*b[1])

