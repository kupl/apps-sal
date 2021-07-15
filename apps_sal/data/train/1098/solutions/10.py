for _ in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 ans = 0
 while a:
  try:
   ans += max(a)
   # pos = a.index(max(a))
   a.remove(max(a))
   a.remove(max(a))
  except:
   break
 print(ans)

