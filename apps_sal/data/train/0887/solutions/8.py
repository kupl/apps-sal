def check_claim(A, B, n):
 if A[0] or B[-1]:
  return False
 if A[-1] != B[0]:
  return False
 if n == 2:
  return True
 for i in range(1, n-1):
  l1, l2, l3 = B[0], A[i], B[i]
  if l1 > l2+l3 or l2 > l1+l3 or l3 > l1+l2 or l1*l2*l3 == 0:
   return False
 return True

t = int(input())
for test in range(t):
 n = int(input())
 A = [int(x) for x in input().split()]
 B = [int(x) for x in input().split()]
 if check_claim(A, B, n):
  print("Yes")
 else:
  print("No")
