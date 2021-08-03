from collections import deque

n, m = [int(i) for i in input().split()]
list_inp = input().split()

D = deque()
ways = 0
Sum = 0

for i in range(n - 1):
    while Sum + int(list_inp[i + 1]) - int(list_inp[i]) > m and len(D) > 0:
        Sum -= D.popleft()

    if Sum + int(list_inp[i + 1]) - int(list_inp[i]) <= m:
        ways += int(len(D) * (len(D) + 1) / 2)
        D.append(int(list_inp[i + 1]) - int(list_inp[i]))
        Sum += D[-1]

print(ways)
