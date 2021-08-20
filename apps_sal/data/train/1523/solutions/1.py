n = int(input())
l = list(map(int, input().split()))
temp = []
for i in range(0, len(l)):
    temp.append(0)
temp[0] = l[0]
temp[1] = l[1]
temp[2] = l[2]
if n <= 3:
    print(sum(temp))
else:
    for i in range(3, n):
        temp[i] = l[i] + min(temp[i - 1], temp[i - 2], temp[i - 3])
    res = sum(l) - min(temp[n - 1], temp[n - 2], temp[n - 3])
    print(res)
