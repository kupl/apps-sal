import heapq
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))


def write(x):
    return sys.stdout.write(x + '\n')


n = int(input())
a = list(map(int, input().split()))
a = [(-num, i) for (i, num) in enumerate(a)]
a.append((0, -1))
heapq.heapify(a)
ans = [0] * n
(pnum, pi) = heapq.heappop(a)
pnum *= -1
count = 1
v = pnum
while a:
    (num, i) = heapq.heappop(a)
    num *= -1
    if i < pi:
        ans[pi] = v - num * count
        v = num * (count + 1)
        count += 1
        pi = i
    else:
        count += 1
        v += num
write('\n'.join(map(str, ans)))
