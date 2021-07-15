t = int(input())
#nsum = [ z*(z+1)/2 for z in xrange(1001)]
for i in range (t):
 n = int(input())
 a = input().split()
 a = [ int(x) for x in a]
 if n==1:
  print('0')
  continue
 pos = {}
 for j in range(n):
  if pos.get(a[j],[])==[]:
   for k in range(j+1,n):
    if a[j] == a[k] :
     pos[a[j]] = pos.get(a[j],[]) + [k]
 total = 0
 for j in range(n-1):
  ar = []
  for k in range(j,-1,-1):
   for x in pos.get(a[k],[]):
    if x>j:
     ar += [x]
   ar.sort()
   if len(ar) > 0:
    total += (ar[0] - j-1)*(ar[0]-j)/2 + (n - ar[-1]-1)*(n-ar[-1])/2
    #print ar
    #print (ar[0] - j-1)*(ar[0]-j)/2 + (n - ar[-1]-1)*(n-ar[-1])/2
   else:
    total += (n-j-1)*(n-j)/2
    #print ar
    #print (n-j-1)*(n-j)/2
   for x in range(len(ar[0:-1])):
    total = total + (ar[x+1]-ar[x]-1)*(ar[x+1]-ar[x])/2
    #print (ar[x+1]-ar[x]-1)*(ar[x+1]-ar[x])/2
 print(total)
