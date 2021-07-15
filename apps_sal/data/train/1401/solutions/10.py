n,k=list(map(int,input().split()))
p=[int(x) for x in input().split()]
p.sort()
i=0
while(k>0):
 k=k-p[i]
 i=i+1
print(i-1) 

