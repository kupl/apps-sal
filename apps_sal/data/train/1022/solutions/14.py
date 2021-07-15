for _ in range(int(input())):
 n, ans = int(input()), "YES"
 a = list(map(int, input().split()))
 if n & 1:
  ans = "NO"
 else:
  for i in range(n>>1):
   opp = i + (n>>1)
   if a[i] != -1 and a[opp] != -1 and a[i] != a[opp]:
    ans = "NO"
    break
   elif a[i] == -1 and a[opp] != -1:
    a[i] = a[opp]
   elif a[i] != -1 and a[opp] == -1:
    a[opp] = a[i]
   elif a[i] == -1 and a[opp] == -1:
    a[i] = 1
    a[opp] = 1
 print(ans)
 if ans == "YES":
  print(*a)
