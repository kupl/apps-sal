from sys import stdin
from collections import Counter


def func(arr, n, l):
    count = 0
    k = l // n
    if n < len(arr):
        for ele in arr[0:n]:
            count += max(0, k - ele)
    else:
        for ele in arr:
            count += max(0, ele - k)
    return count


for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    d = Counter(s)
    arr = sorted(list(d.values()), reverse=True)
    l = len(s)
    val = [1]
    for i in range(2, 27):
        if l % i == 0:
            val.append(i)
    ans = float('inf')
    for ele in val:
        x = func(arr, ele, l)
        if x < ans:
            ans = x
    print(ans)
