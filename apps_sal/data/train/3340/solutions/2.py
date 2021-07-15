key=lambda n:[(0,e:=n&-n,n//e),(1,-n)][e==n]
sharkovsky=lambda a,b:key(a)<key(b)
