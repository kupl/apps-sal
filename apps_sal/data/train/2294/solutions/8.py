n=int(input())
x,y=zip(*sorted(sorted(map(int,input().split())) for _ in range(n)))
p=max(range(n),key=lambda i:y[i])
r=a=x[-1]
b=d=10**9
for i in range(p):
    if b<=x[i]:
        break
    a=max(a,y[i])
    b=min(b,y[i])
    d=min(d,a-min(b,x[i+1]))
print(min((x[-1]-x[0])*(y[p]-min(y)),(y[p]-x[0])*d))
