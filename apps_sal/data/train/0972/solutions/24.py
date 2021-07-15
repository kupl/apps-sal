n, k = map(int, input(). split())
trees = [] 

for i in range(n):
      trees. append(int(input()))

trees.sort() 
minimum = 10**5 

for i in range(0, n - k + 1, 1):
      temp = trees[i + k - 1]  - trees[i]
      minimum = min(temp, minimum)

print(minimum )
