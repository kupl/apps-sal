t= int(input())
for i in range(t):
 n,q = list(map(int,input().split()))
 ans = (n+q+1)*q/(q+1)
 print(ans)

