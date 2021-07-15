for _ in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 res = 0
 gas = a[0]
 for i in range(1, len(a)):
  if gas <= 0:
   break
  else:
   gas -= 1
   res += 1
   gas += a[i]
 print(res + gas)
