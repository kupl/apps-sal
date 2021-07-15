# cook your code here
T = int(input())
for _ in range(T):
 N = int(input())
 A = [0]*N
 for i in range(N):
  s = input()
  ca = 0
  cb = 0
  for x in s:
   if x == 'a':
    ca += 1
   else:
    cb += 1
  A[i] = min(ca,cb)
 print(min(A))

