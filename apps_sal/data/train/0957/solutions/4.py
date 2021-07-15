def Testcase():
 n = int(input())
 li = list(map(int,input().split()))[:n]
 
 if n==2:
  print(abs(li[1]-li[0]))
  return
 
 li.sort()
 ans =0
 for i in range(1,n-1):
  prev = abs(li[i]-li[i-1])
  next = abs(li[i+1]-li[i])
  curr = min(prev,next)
  ans = max(ans,curr)
 
 ans = max(ans,abs(li[1]-li[0]))
 ans = max(ans,abs(li[n-1]-li[n-2]))
 print(ans)
    




t = int(input())
for i in range(t):
 Testcase()
