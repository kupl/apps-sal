import sys

N, K = list(map(int, sys.stdin.readline().split()))
open = [False for i in range(N + 1)]
count = 0

for i in range(K):
    line = sys.stdin.readline().split()
    if len(line) == 1:
        count = 0
        open = [False for i in range(N + 1)]
    else:
        action, num = line
        num = int(num)
        if open[num]:
            count -= 1
        else:
            count += 1
        open[num] = not open[num]
    print(count)
