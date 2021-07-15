import math
def prime(aa):
	f=0
	for y in ar:
		if aa%y==0:
				return 0
	return 1
ar=[]
ar.append(2)
pc=3
te=int(input())
for _ in range(te):
	a=int(input())
	f=0
	c=0
	add=0
	for x in ar:
		try:
			add=add+ar[x-1]
		except:
			while True:
				if prime(pc)==1:
					ar.append(pc)
					if x<=len(ar):
						break
				pc+=1
			pc+=1
			add=add+ar[x-1]
		c+=1
		if c==a:
			break
	print(add)

