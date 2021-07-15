n = int(input().rstrip())

while(n > 0):
 t = int(input().rstrip())
 r = 2 ** t
 r = list(str(r))
 s = 0
 for i in r:
  s = s + int(i)
 print(s)
 n = n-1
