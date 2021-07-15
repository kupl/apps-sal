__author__ = 'Think'
n=int(input())
aints=[int(i) for i in input().split()]
permutes=[int(i)-1 for i in input().split()]
results=[0]

rebuilt={}
m=0
for numby in range(n-1, 0, -1):
	p=permutes[numby]
	below=False
	above=False
	if p-1 in rebuilt:
		below=True
	if p+1 in rebuilt:
		above=True
	if above and below:
		bsum, bottom=rebuilt[p-1]
		asum, top=rebuilt[p+1]
		new=bsum+asum+aints[p]
		rebuilt[bottom]=(new, top)
		rebuilt[top]=(new, bottom)
	elif above or below:
		if above:
			other=p+1
		else:
			other=p-1
		psum, prev=rebuilt[other]
		new=psum+aints[p]
		rebuilt[prev]=(new, p)
		rebuilt[p]=(new, prev)
	else:
		new=aints[p]
		rebuilt[p]=(new, p)
	m=max(new, m)
	results.append(m)
for numby in range(n-1, -1, -1):
	print(results[numby])



