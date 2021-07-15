# cook your dish here
d = {'january':31,'february':29,'march':31,
 'april':30,'may':31,'june':30,'july':31,
 'august':31,'september':30,'october':31,
 'november':30,'december':31}
 
#l=[[15,'january'],[31,'august'],[10,'october']]
l2 = list(d.keys())
for _ in range(int(input())):
 l=input().split()
 l[0]=int(l[0])
 a = l[1]
 ind = l2.index(a)
 b = 183 - (d[l[1]] - l[0])
 while b!=0:
  if ind!=11:
   ind+=1
  else:
   ind = 0
  if b<=d[l2[ind]]:
   print(b,l2[ind])
   break
  b-=d[l2[ind]]
