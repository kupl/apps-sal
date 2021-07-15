n,q,k = map(int,input().split())
l = list(map(str,input().split()))
s = input()
for x in s:
 if x=="!":
  temp = l[-1]
  l[1:] = l[:-1]
  l[0] = temp
  continue
 elif x=="?":
  s_new = "".join(l[:])
  l_new = s_new.split("0")
  l_new.sort()
  if len(l_new[-1])>=k:
   print(k)
  else:
   print(len(l_new[-1]))
