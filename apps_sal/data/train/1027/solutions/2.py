t = int(input())
for i in range(t):
 n, p= list(map(int, input().split()))
 if p == 1 or p == 2:
  print('impossible')
 else:
  s = ''
  if p%2 == 0:
   s = 'a' + 'b'*(p-2) + 'a'
   s = s*(n//p)
  else:
   s = 'a'*(p//2) + 'b' + 'a'*(p//2)
   s = s*(n//p)
  print(s)

