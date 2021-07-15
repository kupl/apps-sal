from itertools import chain
n=int(input())
print("NYOE S"[n%2::2])
v=list(chain.from_iterable((i,i+1) for i in range(1,2*n)if(i%4==0)))
c=list(map((lambda a: a-1 if(a%2==0) else a+1),v))
if(n%2!=0):print(1,*v,2,*c)
