t = int(input())
while (t > 0):
 t -= 1
 n = int(input())
 bits = [0] * n
 mat = []
 for i in range (n):
  mat.append([int(x) for x in input().split()])
 
 for j in range(n):
  if mat[0][j] != (j+1):
   bits[j] = 1
 ans = 0
 count = 0
 for i in range(n-1,0,-1):
  if bits[i] != count:
   ans += 1
   count = (count + 1)%2
 
 print(ans)
 

