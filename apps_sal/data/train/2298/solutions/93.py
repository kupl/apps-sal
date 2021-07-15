_,_,*a=map(int,open(0).read().split());d={}
for x,y in zip(a,__import__("itertools").accumulate(a,min)):d[x-y]=d.get(x-y,0)+1
print(d[max(d.keys())])
