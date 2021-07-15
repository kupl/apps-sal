from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))

p = []
result = []
for x in a:
    r = bisect_left(p, -x)
    if r == len(result):
        result.append([])
        p.append(0)

    result[r].append(x)
    p[r] = -x

for arr in result:
    for i in range(len(arr)-1):
        print(arr[i], end=" ")
    print(arr[-1])
