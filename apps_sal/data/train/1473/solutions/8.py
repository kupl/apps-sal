import sys
import itertools as it

def main():
 t=int(input())
 while t>0:
  t-=1
  r,c,m,k,j=list(map(int,input().split()))
  if m+k+j!=r*c:
   print('No')
  else:
   l=[m,k,j]
   l=list(it.permutations(l))
   chk=0
   for x in l:
    f=test(x,r,c) + test(x,c,r)
    if f>=1:
     chk=1
     break
   if chk==1:
    print('Yes')
   else:
    print('No')
def test(l,r,c):
 for x in range(2,0,-1):
  if l[x]%r==0:
   d=l[x]/r
   c=c-d
  elif l[x]%c==0:
   d=l[x]/c
   r=r-d
  else:
   return 0
  #print r,l,c
  if r==0 or c==0:
   return 0
 if r*c==l[0]:
  return 1
 else:
  return 0

def __starting_point():
 main()

__starting_point()
