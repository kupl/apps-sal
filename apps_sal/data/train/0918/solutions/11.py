mod = 8589934592
def modexp(a, b):
	ans = 1
	while(b != 0):
		if(b % 2 == 1):
			ans = (ans * a)%mod
		a = (a * a)%mod
		b = b // 2
	return ans
t = int(input())
for i in range(t):
	n = int(input())
	print("Case", i+1, end="")
	print(":",(modexp(2,n) - 1 + mod)%mod)

