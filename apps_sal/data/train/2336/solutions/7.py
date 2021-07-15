import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))

swaps = 0
visited = set()
for index in range(n):
    if index in visited:
        continue
    else:
        visited.add(index)
        length = 0
        value = nums[index]
        while (value != index + 1):            
           visited.add(value - 1)
           value = nums[value - 1]
           length += 1
        swaps += length

if ((3 * n - swaps) % 2):
    print("Um_nik")
else:
    print("Petr")





