n=int(input())
a=list(map(int,input().split()))

X=[]
b=a[0]
for i in range(1,n) :
    b^=a[i]

for i in range(n) :
    x=b^a[i]
    X.append(x)

for i in X :
    print(i,end=" ")

