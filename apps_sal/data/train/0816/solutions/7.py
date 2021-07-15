n= int(input())
a=list(map(int,input().strip().split()))
t= int(input())
for i in range(t):
    j=int(input())
    print(a.pop(j-1))
