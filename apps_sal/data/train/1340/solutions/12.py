for _ in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 ans = 0
 count = 0
 for i in a:
  if i > 0:
   ans += i
   count += 1
 res = []
 for i in range(count):
  if a[i] <= 0:
   res.append(i + 1)
 for i in range(count, n):
  if a[i] > 0:
   res.append(i + 1)
 print(ans)
 print(len(res), end=" ")
 print(*res)
