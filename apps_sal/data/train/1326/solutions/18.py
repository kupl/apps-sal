for _ in range(int(input())):
 n = int(input())
 ar = list(map(int, input().split()))
 res = 0
 gas = ar[0]
 for i in range(1, len(ar)):
  if gas==0:
   break
  else:
   gas -= 1
   gas += ar[i]
   res += 1
 res += gas
 print(res)
