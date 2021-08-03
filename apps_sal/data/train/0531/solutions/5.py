n = int(input())
res = []
for _ in range(n):
    res.append(list(map(int, input().split())))
if n == 1:
    print(1)
    return
if n == 2:
    print(2)
    return
start = 2
for i in range(1, n - 1):
    # first check left
    if (res[i][0] - res[i][1]) > res[i - 1][0]:
        # print(res[i])
        #print(abs(res[i][0] - res[i][1]))
        #print(res[i - 1][0])
        start += 1
        continue
    # check right
    if res[i][0] + res[i][1] < res[i + 1][0]:
        #print(res[i], res[i])
        res[i][0] += res[i][1]
        start += 1
        continue
print(start)
