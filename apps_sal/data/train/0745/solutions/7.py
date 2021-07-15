for _ in range(int(input())):
 n = int(input())
 h = list(map(int,input().split()))
 s = sum(h); h[0] = 1
 for i in range(1,n):
  if h[i]>h[i-1]+1:
   h[i] = h[i-1]+1
 h[n-1] = 1
 for i in range(n-2,-1,-1):
  if h[i]>h[i+1]+1:
   h[i] = h[i+1]+1
 print(s-max(h)**2)
