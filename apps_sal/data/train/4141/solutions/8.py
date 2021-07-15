from math import*;solve=lambda x,y:len({2**m*3**n+1
for n in range(0,ceil(log(y-1,3)))
for m in range(ceil(log(max(~-x/3**n,1),2)),ceil(log(~-y/3**n,2)))
if all((2**m*3**n+1)%d for d in range(2,int((2**m*3**n+1)**.5)+1))})
