#from __future__ import division


nCr = [[0 for x in range(1001)] for x in range(1001)]
 
for i in range (0,1001):
 nCr[i][0]=1
 nCr[i][i]=1
for i in range (1,1001):
 for j in range (1,1001):
  if i!=j:
   nCr[i][j] = nCr[i-1][j] + nCr[i-1][j-1]
'''
def comb(n,r):
    if r>n :
     return 0
    else :
     i = n
     j = 0
     p = 1
     if r>n-r :
      r=n-r
     t=range(1,r+1)
     #print t
     for j in t:
      p=p*i
      p=p/j
      i=i-1
     return p
'''
def main():
 t=int(input())
 #print t
 for i in range(t):
  num=0
  line = input().split(" ")
  #print line
  s = int(line[0])
  n = int(line[1])
  m = int(line[2])
  k = int(line[3])
  #print k
  if k>n-1:
   print("0.000000")
  else:
   j=k
   while j<n and j<m :
    p = int(nCr[m-1][j])
    q = int((nCr[s-m][n-j-1]))
    #print p,q
    num = int(num) + (p*q)
    j=j+1
   den=int(nCr[s-1][n-1])
   #print num,den
   ans=float(num)/den
   print('{0:.10f}'.format(ans))
 # my code here
 
def __starting_point():
 main()
__starting_point()
