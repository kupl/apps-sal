'''input
3 3
100 100 100
100 1 100
100 100 100
'''
# again a coding delight
from sys import stdin


def create_dp1(matrix, n, m):
	dp = [[0 for i in range(m)] for j in range(n)]
	for i in range(n):
		for j in range(m):
			if i - 1 >= 0:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i - 1][j])
			if j - 1 >= 0:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i][j - 1])
			elif i - 1 < 0 and j - 1 < 0:
				dp[i][j] = matrix[i][j]
	return dp


def create_dp2(matrix, n, m):
	dp = [[0 for i in range(m)] for j in range(n)]
	for i in range(n - 1, -1, -1):
		for j in range(m - 1, -1, -1):
			if i + 1 < n:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i + 1][j])
			if j + 1 < m:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i][j + 1])
			if i + 1 >= n and j + 1 >= m:
				dp[i][j] = matrix[i][j]
	return dp 


def create_dp3(matrix, n, m):
	dp = [[0 for i in range(m)] for j in range(n)]
	for i in range(n - 1, -1, -1):
		for j in range(m):
			if i + 1 < n:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i + 1][j])
			if j - 1 >= 0:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i][j - 1])
			if i + 1 >= n and j - 1 < 0:
				dp[i][j] = matrix[i][j]
	return dp 


def create_dp4(matrix, n, m):
	dp = [[0 for i in range(m)] for j in range(n)]
	for i in range(n):
		for j in range(m - 1, -1, -1):
			if i - 1 >= 0:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i - 1][j])
			if j + 1 < m:
				dp[i][j] = max(dp[i][j], matrix[i][j] + dp[i][j + 1])
			if i - 1 < 0 and j + 1 >= m:
				dp[i][j] = matrix[i][j]
	return dp 


# main starts
n, m = list(map(int, stdin.readline().split()))
matrix = []
for _ in range(n):
	matrix.append(list(map(int, stdin.readline().split())))

dp1 = create_dp1(matrix, n, m) # from 0, 0 to i, j
dp2 = create_dp2(matrix, n, m) # from i, j to n, m
dp3 = create_dp3(matrix, n, m) # from n, 1 to i, j
dp4 = create_dp4(matrix, n, m) # from i, j to 1, m

total = -float('inf')
for i in range(1, n - 1):
	for j in range(1, m - 1):
		first = dp1[i - 1][j] + dp2[i + 1][j] + dp3[i][j - 1] + dp4[i][j + 1]
		second = dp1[i][j - 1] + dp2[i][j + 1] + dp3[i + 1][j] + dp4[i - 1][j]
		total = max(total, first, second)
print(total)
