# cook your dish here
import math
def swap(a,b):
 return b,a

t = int(input())
while(t!=0):
 z = list(map(int,input().strip().split(" ")))
 x=z[0]
 r=z[1]
 a=z[2]
 b=z[3]
 #p = math.pi
 peri = 2*r
 tp = x*peri
 
 if(a<b):
  a,b=swap(a,b)
 t1 = tp/a
 d2 = t1* b
 dd = abs(tp-d2)
 
 if(dd%peri==0):
  print(int(dd//peri)-1)
 else:
  n = int(dd//peri)
  print(n)
 t-=1
