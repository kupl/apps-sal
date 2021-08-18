from bisect import insort
from math import ceil
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    ans = 0
    index = []
    for i in range(1, n + 1):
        index.append(ceil(k / (ceil(k / i))))
    for i in range(n):
        count = [0] * (2001)
        temp = []
        for j in range(i, n):
            count[array[j]] += 1
            insort(temp, array[j])
            x = temp[index[j - i] - 1]
            f = count[x]
            if count[f]:
                ans += 1
    print(ans)
