n = int(input())
g = [int(g) for g in input().split()]
xor = 0
arr = [[0] * (2**20), [1] + [0] * (2**20 - 1)]
count = 0
for i in range(len(g)):
    xor ^= g[i]
    count += arr[i % 2][xor]
    arr[i % 2][xor] += 1
print(count)
