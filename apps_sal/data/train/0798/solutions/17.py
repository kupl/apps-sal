n , m = map(int, input().split())
grid = []
grid_charm = []
cost = []
for i in range(n):
	hehe = [0 for jj in range(n)]
	maggi = [0 for jj in range(n)]
	row = list(map(int , input().split()))
	grid.append(row)
	grid_charm.append(hehe)
	cost.append(maggi)

for i in range(m):
	x , y , k = map(int, input().split())
	x , y = x-1 , y-1
	for j in range(k+1):
		for z in range(k +1):
			if not j + z  <= k:
				break 
			alpha , beta , gamma, lol = x-j , y-z , x + j , y + z
			if alpha >=0:
				if beta >=0:
					grid_charm[alpha][beta] = 1
				if lol < n:
					grid_charm[alpha][lol] = 1
			if beta >= 0:
				if gamma < n:
					grid_charm[gamma][beta] = 1
			if gamma < n:
				if lol < n:
					grid_charm[gamma][lol] = 1


# for i in grid_charm:
# 	print(*i)
cost[0][0] = grid[0][0]	
for i in range(n):
	for j in range(n):
		lol = -999999999999

		if i > 0:
			if grid_charm[i-1][j] == 1 and cost[i-1][j] != -999999999999:
				lol = max(lol , grid[i][j] + cost[i-1][j])

		if j > 0:
			if grid_charm[i][j-1] == 1 and cost[i][j-1] != -999999999999:
				lol = max(lol , grid[i][j] + cost[i][j-1])


		if grid_charm[i][j] == 0:
			cost[i][j] = -999999999999
		else:
			if not(i == 0 and j ==0):
				cost[i][j] = lol

# for i in cost:
# 	print(*i)
if cost[n-1][n-1] == -999999999999:
	print('NO')
else:
	print('YES')
	print(cost[n-1][n-1])








