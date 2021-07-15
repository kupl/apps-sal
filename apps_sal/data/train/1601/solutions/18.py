# cook your dish here
from sys import stdin,stdout

l_in = stdin.readline
l_out = stdout.write

  
t = int(l_in())

for i in range(t):
 MaxM = 0
 count = 0
 N,P = list(map(int,(l_in().strip().split())))
 ar = list(range(1,P+1))
 #print(ar)
 for i in ar:#range(P):
  for j in ar:#range(P):
   for k in ar:#range(P):
    M = (((N%i)%j)%k)%N
    if M > MaxM:
     count = 1
     MaxM = M
     #print("{} {} {} {}".format(i,j,k,MaxM))
    elif M == MaxM:
     count = count + 1
     #print("{} {} {} {}".format(i,j,k,MaxM))
 print(count)
 

