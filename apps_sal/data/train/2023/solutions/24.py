import math
n = int(input())
t = range(1, n + 1)
size = math.floor(math.sqrt(n))
ans = [list(t[i:i + size])[::-1] for i in range(0, n, size)]
for i in ans:
    for j in i:
        print(j, end=' ')
print(end='\n')
