# cook your dish here
t=int(input().strip())
for _ in range(t):
 n = int(input().strip())
 a = list(map(int,input().strip().split(" ")))
 a.sort(reverse=True)
 ans = 0
 for i in range(0,n,2):
  ans += a[i]
 print(ans)
