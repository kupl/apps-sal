# cook your dish here
try:
 for _ in range(int(input())):
  s, n = map(int, input().split())
  if s > n:
   c = s // n
   r = s % n
   if r == 0:
    print(c)
   elif r == 1:
    print(c + 1)
   elif r % 2 == 0:
    print(c + 1)
   else:
    print(c + 2)
  else:
   if s % 2 == 0:
    print("1")
   else:
    if s == 1:
     print("1")
    else:
     print("2")
except:
 pass
