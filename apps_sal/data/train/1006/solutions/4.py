t = int(input())
for i in range(t):
 l = list(map(int, input().split()))
 s = str(l[0])
 while 1:
  s = s+str(l[1])
  for x in range(len(s)-1):
   if s[x]>s[x+1]:
    s=s[:x]+s[x+1:]
    break
  else:
   s = s[:len(s)-1]
   break
 print(int(s))

