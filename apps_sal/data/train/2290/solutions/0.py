import sys
def input():
	return sys.stdin.readline()[:-1]

H, W = map(int, input().split())
s = [input() for _ in range(H)]
ans = max(H, W)

def max_rect(a):
	res = 0
	stack = [a[0]]
	for i in range(1, W-1):
		new_pos = i
		while stack and stack[-1] % 10000 >= a[i]:
			pos, hght = stack[-1] // 10000, stack[-1] % 10000
			res = max(res, (i - pos + 1) * (hght + 1))
			new_pos = pos
			stack.pop()
		stack.append(new_pos * 10000 + a[i])
	while stack:
		pos, hght = stack[-1] // 10000, stack[-1] % 10000
		res = max(res, (W - pos) * (hght + 1))
		stack.pop()
	return res

dp = [[0 for _ in range(W-1)] for _ in range(H-1)]

for j in range(W-1):
	if not ((s[0][j] == s[1][j]) ^ (s[0][j+1] == s[1][j+1])):
		dp[0][j] = 1
ans = max(ans, max_rect(dp[0]))

for i in range(1, H-1):
	for j in range(W-1):
		if not ((s[i][j] == s[i+1][j]) ^ (s[i][j+1] == s[i+1][j+1])):
			dp[i][j] = dp[i-1][j] + 1
	ans = max(ans, max_rect(dp[i]))

print(ans)
