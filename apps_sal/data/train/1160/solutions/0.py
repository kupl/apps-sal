def get(l,n):
 l1,l2 = [],[]
 i = 1
 h1,m1 = l[0]
 while (i < len(l)):
  h2,m2 = l[i]
  if (h1>h2):
   if (m1 >= m2):
    l1 += [(0,10**20)]
    l2 += [(-1,-1)]
   else:
    d = (h1-h2)//(m2-m1)
    if (((h1-h2)%(m2-m1)) == 0):
     l1 += [(0,d-1)]
     l2 += [(d+1,10**20)]
    else:
     l1 += [(0,d)]
     l2 += [(d+1,10**20)]
  elif(h1==h2):
   if (m1 > m2):
    l1 += [(1,10**20)]
    l2 += [(-1,-1)]
   elif(m1==m2):
    l1 += [(-1,-1)]
    l2 += [(-1,-1)]
   else:
    l2 += [(1,10**20)]
    l1 += [(-1,-1)]
  else:
   if (m1 <= m2):
    l2 += [(0,10**20)]
    l1 += [(-1,-1)]
   else:
    d = (h2-h1)//(m1-m2)
    if ((h2-h1)%(m1-m2) == 0):
     l2 += [(0,d-1)]
     l1 += [(d+1,10**20)]
    else:
     l2 += [(0,d)]
     l1 += [(d+1,10**20)]
  i += 1
  h1,m1 = h2,m2
 return l1,l2
 
def intersect(k1,k2):
 k1,k2 = min(k1,k2),max(k1,k2)
 c1,c2 = k1
 c3,c4 = k2
 l = [c1,c2,c3,c4]
 l.sort()
 if (l[2]==c2):
  return (c3,min(c2,c4))
 elif (l[3]==c2):
  return k2
 else:
  return (-1,-1)
 
 
 
def union(k1,k2):
 k1,k2 = min(k1,k2),max(k1,k2)
 c1,c2 = k1
 c3,c4 = k2
 l = [c1,c2,c3,c4]
 l.sort()
 if (c2==l[3]):
  return ([c1,c2])
 elif(c2==l[2] or ((c3-c2) == 1)):
  return([c1,c4])
 else:
  return([c1,c2,c3,c4])
 
 
def aa(l1,l2,n):
 c1,c2 = 0,10**20
 i = 0
 n -= 1
 while (i < n):
  if (i%2 == 0):
   k1,k2 = l1[i]
  else:
   k1,k2 = l2[i]
  i += 1
  if ((k1,k2) == (-1,-1)):
   return (-1,-1)
  c1,c2 = intersect((c1,c2),(k1,k2))
  if ((c1,c2) == (-1,-1)):
   return (c1,c2)
 return (c1,c2)
 
 
test = int(input())
while (test != 0):
 test -= 1
 n = int(input())
 l = []
 i = 0
 while (i < n):
  c1,c2 = list(map(int,input().split()))
  l += [(c1,c2)]
  i += 1
 if (n == 1):
  print(1)
  print("0 Inf")
 else:
  l1,l2 = (get(l,n))
  k1,k2 = aa(l1,l2,n)
  if ((k1,k2) == (-1,-1)):
   k1,k2 = aa(l2,l1,n)
   if ((k1,k2) == (-1,-1)):
    print(0)
   else:
    print(1)
    if (k2 == 10**20):
     k2 = "Inf"
    print(str(k1) + " " +str(k2))
  else:
   k3,k4 = aa(l2,l1,n)
   if ((k3,k4) == (-1,-1)):
    print(1)
    if (k2 == 10**20):
     k2 = "Inf"
    print(str(k1) + " " +str(k2))
   else:
    p = union((k1,k2),(k3,k4))
    if (len(p)==2):
     c1,c2 = p
     if (c2==10**20):
      c2 = "Inf"
     print(1)
     print(str(c1) + " " +str(c2))
    else:
     c1,c2,c3,c4 = p
     if (c4 == 10**20):
      c4 = "Inf"
     print(2)
     print(str(c1) + " " +str(c2))
     print(str(c3) + " " +str(c4))

