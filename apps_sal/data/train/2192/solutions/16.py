N = int(input())
d = [0 for i in range(1000001)]
Memo = [0 for i in range(1000001)]
max_pos = 0
for i in range(N):
    subList = input().split()
    index = int(subList[0])
    d[index] = int(subList[1])
    max_pos = max(index, max_pos)
if (d[0] != 0):
    Memo[0] = 1

result = N
result = min(result, N - Memo[0])

for i in range(1, max_pos + 1):
    if d[i] == 0:
        Memo[i] = Memo[i - 1]
    else:
        if d[i] >= i:
            Memo[i] = 1
        else:
            Memo[i] = Memo[i - d[i] - 1] + 1
    result = min(result, N - Memo[i])
print(result)
