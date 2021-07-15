def check(x, a) :
	tmp = a;
	for i in x:
		tmp = tmp - (a-i);
		

	if tmp <= 0:
		return 1;
	else: return 0;


n=int(input())
x=[int(a) for a in input().split()]
#for i in range(0,n):
#	x.append(int(input()));

# x.sort();
#for i in range(0,n):
#	print(x[i])

l = max(x);
h = 100000000000000000000;

while (l <= h) :
	mid = (l+h) // 2;
	c = check(x,mid);
	if c > 0:
		h = mid-1;
	else: l = mid+1;

print(l);
