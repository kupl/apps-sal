import numpy as np
l = input().split()
n=int(l[0])
m=int(l[1])
l=[]
for _ in range(n):
 l.append(list(map(int,input().split()))[:])
tc = int(input())
arr = np.array(l)
for _ in range(tc):
 dim = input().split()
 r1 = int(dim[0])
 c1 = int(dim[1])
 r2 = int(dim[2])
 c2 = int(dim[3])
 t = arr[r1-1:r2,c1-1:c2]
 print(np.sum(t))
 

