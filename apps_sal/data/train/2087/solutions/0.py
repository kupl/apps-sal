import sys
3


n, l, r, ql, qr = list(map(int, sys.stdin.readline().strip().split()))
w = [int(x) for x in sys.stdin.readline().strip().split()]

s = [0]
for i in range(0, n):
    s.append(s[-1] + w[i])


def cost(left):
    right = n - left
    diff = left - right
    bonus = 0
    if diff > 0:  # left part is larger
        bonus = ql * (diff - 1)
    elif diff < 0:  # right part is larger
        bonus = qr * (-diff - 1)
    return bonus + l * s[left] + r * (s[n] - s[left])


best = cost(0)
for left in range(1, n + 1):
    c = cost(left)
    if c < best:
        best = c

print(best)
