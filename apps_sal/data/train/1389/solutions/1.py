def ff(z):
	x="";l=['.','!',',',';',':','\n',"'",'  ']
	for i in str(z):
		if i not in l and (ord(i)!=32 or ord(i)!=10):
			x+=i
	x=x.replace('  ',' ');x=x.split(' ')
	return ' '.join(reversed(x))
n=int(input());li=[]
while n:
	n-=1;li.append(ff(input()))
i=len(li)-1
while i>-1:
	print(li[i]);i-=1
