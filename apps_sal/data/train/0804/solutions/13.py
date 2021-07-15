p2=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216]
for _ in range(int(input())):
	n=int(input())-1
	a=[int(x) for x in input().split()]
	f,l=int(input()),[]
	for i in range(n):
		if a[i]<=f: l.append(i)
		if i%2==0: a.append(a[i])
	if len(l)==0:
		print("impossible")
		continue
	print("possible")
	d,p=10**12,-1
#	print(*a)
	for i in l:
		x=-1+n-i+(i+1)//2
		last=i+x
		td=f
		if i%2==1: td+=a[i-1]
		for j in range(1,25):
			if p2[j]>x: break
			la=last-x%p2[j]
			if la+p2[j-1]>last: td+=a[la]
		if td<d: d,p=td,i+1
	print(p,d)

