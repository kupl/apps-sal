# coding = utf-8
from functools import reduce
div = 1000000007
s = input()
n = int(s)
s = input()
num = list([int(x) for x in s.split(" ")])

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

g = reduce(gcd,num)
m = max(num)

now = m/g
remain = now - len(num)
if remain%2==0:
	print("Bob")
else:
	print("Alice")

