def add(A, B):
 cnt = 0
 while B > 0:
  U = A ^ B
  B = (A & B) * 2
  A = U
  cnt += 1
 return cnt

for _ in range(int(input())):
 print(add(int(input(),2), int(input(), 2)))
