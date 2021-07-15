# v = ["a","e","i","o","u"]
# for _ in range(int(input())):
#   n = int(input())
#   a,b = [],[]
#   for i in range(n):
#       s = input()
#       isa = True
#       for j in range(1,len(s) - 1):
#           if(s[j] in v):
#               if(s[j - 1] not in v and s[j + 1] not in v):
#                   isa = False
#           else:
#               if(s[j - 1] not in v or s[j + 1] not in v):
#                   isa = False
#           if(not isa):
#               break
#       if(s[0] not in v and s[1] not in v):
#           isa = False
#       if(s[-1] not in v and s[-2] not in v):
#           isa = False
#       if(isa):
#           a.append(s)
#       else:
#           b.append(s)
#   dicta,dictb = {},{}
#   for i in a:
#       freq = {}
#       for j in i:
#           if(j in freq):
#               freq[j] += 1
#           else:
#               freq[j] = 1
#       for j in freq:
#           if(j not in dicta):
#               dicta[j] = (1,freq[j])
#           else:
#               dicta[j] = (dicta[j][0] + 1,dicta[j][1] + freq[j])
#   for i in b:
#       freq = {}
#       for j in i:
#           if(j in freq):
#               freq[j] += 1
#           else:
#               freq[j] = 1
#       for j in freq:
#           if(j not in dictb):
#               dictb[j] = (1,freq[j])
#           else:
#               dictb[j] = (dictb[j][0] + 1,dictb[j][1] + freq[j])
#   ans = 1
#   for i in dicta:
#       ans *= dicta[i][0]
#   for i in dictb:
#       ans /= dictb[i][0]
#   x,y = 1,1
#   for i in dictb:
#       x *= dictb[i][1]
#   for i in dicta:
#       y *= dicta[i][1]
#   alice,bob = len(a),len(b)
#   for i in range(bob):
#       while(alice > 0 and ans > 10**7):
#           ans /= y
#           alice -= 1
#       ans *= x
#       if(ans > 10**7 and alice == 0):
#           break
#   while(alice > 0):
#       ans /= y
#       if(ans < 1 and alice > 100):
#           ans = 0
#           break
#       alice -= 1
#   if(ans > 10**7):
#       print("Infinity")
#   else:
#       print(ans)
# #partailly correct [75 pts]
#sys.stdin.readline() and sys.stdout.write() are faster I/O methods than input()     and print()
from sys import stdin
z=['a','i','e','o','u']
t=int(stdin.readline())
while(t>0):
 t-=1
 n=int(stdin.readline())
 alice=[]
 bob=[]
 for j in range(n):
  s=str(stdin.readline().strip("\n"))
  # print(s)
  isalice=True
  for i in range(1,len(s)-1):
   if(s[i] in z):
    if(s[i-1] not in z and s[i+1] not in z):
     isalice=False
   else:
    if(s[i-1] not in z or s[i+1] not in z):
     isalice=False
   if(not isalice):
    break
  if(s[0] not in z and s[1] not in z):
   isalice=False
  if(s[-1] not in z and s[-2] not in z):
   isalice=False
  if(isalice):
   alice.append(s)
  else:
   bob.append(s)
 ali={}
 bo={}
 for i in alice:
  d={}
  for j in i:
   if(j in d):
    d[j]+=1
   else:
    d[j]=1
  for j in d:
   if j not in ali:
    ali[j]=(1,d[j])
   else:
    ali[j]=(ali[j][0]+1,ali[j][1]+d[j])
 for i in bob:
  d={}
  for j in i:
   if(j in d):
    d[j]+=1
   else:
    d[j]=1
  for j in d:
   if j not in bo:
    bo[j]=(1,d[j])
   else:

    bo[j]=(bo[j][0]+1,bo[j][1]+d[j])
 ans=1
 for i in ali:
  ans*=ali[i][0]
 for i in bo:
  ans=ans/bo[i][0]
 x=1
 y=1

 for i in bo:
  x=x*bo[i][1]
 for i in ali:
  y=y*ali[i][1]
 # print(x,y)
 alice=len(alice)
 bob=len(bob)
 for i in range(bob):
  while(alice>0 and ans>10000000):
   ans=ans/y
   alice-=1
  ans*=x
  if(ans>10000000 and alice==0):
   break
 while(alice>0):
  ans=ans/y
  if(ans<1 and alice>100):
   ans=0
   break
  alice-=1
 if(ans>10000000):
  print("Infinity")
 else:
  print(ans)
#AC

