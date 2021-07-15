def not_destroyed(x, n):
 for j in range(n):
  if x[j] == '1':
   x[j] = '2'
   if j-1 >= 0:
    x[j-1] = '2'
   if j+1 < n and x[j+1] != '1':
    x[j+1] = '2'
 return x.count('0')
    

T = int(input())
for i in range(T):
 L = []
 N = int(input())
 S = input()
 for j in range(N):
  L.append(S[j])
 n = not_destroyed(L, N)
 print(n)

