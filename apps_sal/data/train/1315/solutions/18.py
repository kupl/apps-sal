# cook your dish here
import sys
n=int(input().strip())
diz={}
counter=0
for _ in range(n):
    values=list(map(int, input().strip().split()))
    values.sort(reverse=True)
    values=tuple(values)
    if values not in diz:
        diz[values]=1 
        counter+=1 
    else:
        if diz[values]==1:
            counter-=1 
            diz[values]=0
print(counter)

