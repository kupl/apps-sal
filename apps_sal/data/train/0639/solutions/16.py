for _ in range (int(input())):
 s=input()
 t=[]
 for i in set (s):
  t.append(s.count(i))
 t=sorted(t)
 if len(t)<3 or t[-1]==t[-2]+t[-3]:
  print('Dynamic')
 else:
  print('Not')
# cook your dish here

