'''
t=int(input())

l=[]                                    
while t:
    n=int(input())
    while n:
     coor=int(input()),int(input())  
     l.append(coor)
     n-=1
  
    t-=1
    lcopy=sorted(l)
    for i in range(len(l)):
     length=len(lcopy)
     for j in range(i+1,len(l)):
      if abs(l[i][0]-l[j][0])==abs(l[i][1]-l[j][1]):
       if l[j] in lcopy: lcopy.remove(l[j])
     if length!=len(lcopy):
      if l[i] in lcopy: lcopy.remove(l[i])
    print(l)

    print(lcopy)
'''

import cmath
import math


def f(l):
    l1 = []
    for i in range(len(l)):
        w = cmath.polar(l[i])
        z = cmath.rect(w[0], w[1] - cmath.pi / 4)
        l1.append(z)

    l1.sort(key=lambda z: z.real)
    for i in range(len(l1) - 1):
        diff = abs(l1[i].real - l1[i + 1].real)
        if diff == 0:
            print(0)
            return
        if i == 0:
            minDiffX = diff
        else:
            minDiffX = min(diff, minDiffX)

    l1.sort(key=lambda x: x.imag)
    for i in range(len(l1) - 1):
        diff = abs(l1[i].imag - l1[i + 1].imag)
        if diff == 0:
            print(0)
            return
        if i == 0:
            minDiffY = diff
        else:
            minDiffY = min(diff, minDiffY)

    '''d=min(abs(l[0].real-l[1].real),abs(l[0].imag-l[1].imag))
    for i in range(1,len(l1)):
     for j in range(i+1,len(l1)):
      x=min(abs(l[i].real-l[j].real),abs(l[i].imag-l[j].imag))
      if x<d: d=x
'''
    print(min(minDiffX, minDiffY) * math.sin(math.pi / 4))


T = int(input())

while T:
    l = []

    n = int(input())
    while n:
        t = input().split()
        l.append(complex(int(t[0]), int(t[1])))
        n -= 1

    f(l)

    T -= 1
