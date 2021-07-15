n, m, k = [int(n) for n in input().split()]
a = [int(n) for n in input().split()]
instructions = []
temp = []
for i in range(n+1):
	temp.append(0)
for i in range(m):
	instructions.append([int(n) for n in input().split()])
queries = []
for i in range(m+1):
	queries.append(0)
for i in range(k):
	x, y = [int(n) for n in input().split()]
	x-=1
	y-=1
	queries[x]+=1
	queries[y+1]-=1

num_queries = 0
for i in range(m):
	num_queries += queries[i]
	temp[instructions[i][0]-1] += num_queries*instructions[i][2]
	temp[instructions[i][1]] -= num_queries*instructions[i][2]
#print(temp[0]+a[0], end=" ")
x = temp[0]
print(x + a[0], end=" ")
for i in range(1, n):
	x += temp[i]
	print(x + a[i], end=" ")
print()
