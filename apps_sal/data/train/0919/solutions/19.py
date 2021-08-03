'''Author- Akshit Monga'''
from sys import stdin, stdout
input = stdin.readline


def f(arr):
    ans = 0
    val = 0
    s = -1
    for i in arr:
        if i != s:
            ans += val % 2
            val = 1
            s = i
        else:
            val += 1
    ans += val % 2
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n > 18:
        print(f(arr))
        continue
    ans = float('inf')
    for mask in range(0, 1 << n):
        vals = []
        c = 0
        for i in range(n):
            if mask & (1 << i):
                vals.append(arr[i])
            else:
                c += 1
        ans = min(ans, c + f(vals))
    stdout.write(str(ans) + '\n')
