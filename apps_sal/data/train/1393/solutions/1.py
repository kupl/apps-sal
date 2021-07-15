for _ in range(int(input())):
 n = int(input())
 l = list(map(int,input().split()))
 ans = 1
 l1 = l[0]
 for i in range(1,n):
  if l[i] <= l1:
   l1 = l[i]
   ans = ans + 1
 print(ans)
