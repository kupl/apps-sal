from math import*
t=int(input())
s=input()
n=s.count("n")
o=s.count("o")
e=s.count("e")
r=s.count("r")
z=s.count("z")
while o>0 and n>0 and e>0:
    print(1,end=' ')
    n-=1
    o-=1
    e-=1
while z>0:
    print(0,end=' ')
    z-=1
