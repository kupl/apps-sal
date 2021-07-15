def gcd(a,b):
	if b==0:return a
	else:return gcd(b,a%b)
def lcm(a,b):
	m=a*b
	g=gcd(a,b)
	return int(m/g)
for _ in range(int(input())):
	x,y=[int(x) for x in input().split()]
	l=lcm(x,y)
	s=int(l/x)
	t=int(l/y)
	print(s+t-2)
