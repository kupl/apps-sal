# import sys
# sys.stdin = open("F:\\Scripts\\input","r")
# sys.stdout = open("F:\\Scripts\\output","w")


MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))

n , = I()
s = input()
t = input()
ans = 0
i = 0
while i < n:
	if i < n-1 and (s[i]+s[i+1] == '01' and t[i]+t[i+1] == '10' or (s[i]+s[i+1] == '10' and t[i]+t[i+1] == '01')):
		ans += 1
		i += 2
	elif s[i] != t[i]:
		ans += 1
		i += 1
	else:
		i += 1
print(ans)

