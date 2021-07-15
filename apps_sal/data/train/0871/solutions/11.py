def sumOfN(n): return n*(n-1)//2

def display():
	for i in range(r):
		for j in range(c):
			print(grid[i][j], end =" ")
		print()
	
	print()

for t in range(int(input())):
	r,c = map(int,input().split())
	grid = []
	pairs = 0
	for i in range(r):
		to_add = []
		for x in input().strip(): to_add.append([x,1])
		grid.append(to_add)	

	#display()
	steps = max(r,c)
	for _ in range(steps):
		for i in range(r):
			for j in range(c):
				s = grid[i][j][0][:grid[i][j][1]]
				if s=="#" or s=="-":
					continue
				
				for ants in s:
					if ants=="U":
						if i>0:
							if grid[i-1][j][0]!="#": grid[i-1][j][0] += "U"
					elif ants=="D":
						if i<r-1:
							if grid[i+1][j][0]!="#": grid[i+1][j][0] += "D"
					elif ants=="L":
						if j>0:
							if grid[i][j-1][0]!="#": grid[i][j-1][0] += "L"
					elif ants=="R":
						if j<c-1:
							if grid[i][j+1][0]!="#": grid[i][j+1][0] += "R"

				grid[i][j][0] = ("-" if len(grid[i][j][0])==grid[i][j][1] else grid[i][j][0][grid[i][j][1]:])

		for i in range(r):
			for j in range(c):
				if grid[i][j][0].lstrip('-')!="":
					grid[i][j][0] = grid[i][j][0].lstrip('-')
					pairs += sumOfN(len(grid[i][j][0]))
				grid[i][j][1] = len(grid[i][j][0])
		
		#display()
	print(pairs)
