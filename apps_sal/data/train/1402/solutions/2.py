def add(A, B):
 cnt = 0
 while B > 0:
  cnt += 1
  U = A ^ B
  V = A & B
  A = U
  B = V * 2
 return cnt

for _ in range(int(input().strip())):
 print(add(int(input().strip(), 2), int(input().strip(), 2)))
