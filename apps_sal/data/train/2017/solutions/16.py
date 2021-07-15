n=int(input())
li=[*map(int,input().split())]
count=0
while len(li)>0:
	a=li[0]
	li.remove(a)
	count+=li.index(a)
	li.remove(a)
print(count)
