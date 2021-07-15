n=int(input())
x=[]
for i in range(n):
    a=list(map(int,input().split()))
    a.append(i+1)
    x.append(a)
x.sort(key=lambda x:[-sum(x[:4]),x[4]])
for i in range(n):
    if x[i][4]==1:
        print(i+1)
        return
