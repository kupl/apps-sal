from sys import stdin, stdout 
import numpy as np
t = int(stdin.readline())
while t>0:
 t-=1
 n,m = stdin.readline().split()
 n= int(n)
 m = int(m)
 b = [1]*(n+1)
 c = [1]*(n+1)
 b = np.asarray(b)
 c = np.asarray(c)
 while m>0:
  m-=1
  i,j,k = stdin.readline().split()
  i=int(i)
  j=int(j)
  k=int(k)
  b[i-1]*=k;
  c[j]*=k;
 ar = [10]*(n+1)
 ar = np.asarray(ar)
 ar[0] = b[0];
 ar[0]/=c[0];
 for i in range(n):
  ar[i] = ar[i-1];
  ar[i] *= b[i];
  ar[i]/= (c[i]);
 Sum=0
 for i in range(n):
  Sum+=ar[i];
 print(int(Sum/n))

