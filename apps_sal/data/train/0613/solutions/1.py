count = 0
for t in range(int(input())):
 l = []
 s = input()
 for c in s:
  l.append(c)
  if (len(l)==1):
   continue
  else:
   if (l[-1]==l[-2]):
    l = l[:-2]
 if (len(l)==0):
  count+=1
print(count)
