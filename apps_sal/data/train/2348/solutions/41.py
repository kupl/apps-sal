import math
import bisect


def make_tree():
    to = [0] * n
    j = 0
    for i in range(n):
        while x[j + 1] - x[i] <= l:
            j += 1
        to[i] = j
    return to


def binary_lifting():
    m = int(math.log2(n)) + 3
    to2 = [[n - 1] * m for _ in range(n)]
    for i in range(n):
        to2[i][0] = to[i]
    for j in range(1, m):
        for i in range(n):
            to2[i][j] = to2[to2[i][j - 1]][j - 1]
            if to2[i][j] == n - 1:
                break
    return to2


def solve(a, b):
    if a > b:
        a, b = b, a
    ans = 0
    while True:
        i = bisect.bisect_left(to2[a], b)
        if i == 0:
            if not a == to2[a][0]:
                ans += 1
            break
        a = to2[a][i - 1]
        ans += pow2[i - 1]
    return ans


n = int(input())
x = list(map(int, input().split()))
l = int(input())
inf = 1145141919810
m = int(math.log2(n)) + 3
x.append(inf)
to = make_tree()
to2 = binary_lifting()
q = int(input())
pow2 = [1] * m
for i in range(1, m):
    pow2[i] = 2 * pow2[i - 1]
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ans = solve(a, b)
    print(ans)
