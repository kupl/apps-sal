import math
def check(n):
	if n<9:
		return n
	else:
		ans = n%9
		if ans==0:
			return 9
		return ans		

t = int(input())
while t>0:
	t -= 1
	sum = 0
	a,d,l,r = input().split()
	a,d,l,r = int(a),int(d),int(l),int(r)
	dig = r-l+1
	mod = dig%9
	div = int(dig/9)
	nth = a+(l-1)*d                                          
	nth = check(nth)
	temp = 0
	for i in range(l,min(l+8,r)+1):
		temp += 1
		mul = 0 if temp>mod else 1
		sum += nth*(div+mul)
		nth = check(nth+d)
	print(int(sum))
