def gcd(x,y):
 if(x==0):return y
 return gcd(y%x,x)

t = int(input())

for _ in range(t):
 n = int(input())
 l = list(map(int,input().split()))
 pre = [0]*n
 pre[0] = l[0]
 for i in range(1,n):
  pre[0] = gcd(l[i],pre[0])
 if(pre[0]==1):print(n)
 else:print(-1)


 

























