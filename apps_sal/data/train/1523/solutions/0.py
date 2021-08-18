n = int(input())
l = list(map(int, input().split()))
temp = []
for item in l:
    temp.append(item)
if(n <= 3):
    print(sum(temp))
else:
    for i in range(3, n):
        temp[i] = l[i] + min(temp[i - 1], temp[i - 2], temp[i - 3])
    res = sum(l) - min(temp[n - 1], temp[n - 2], temp[n - 3])
    print(res)
