import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None] * T
for qu in range(T):
    x1, y1, x2, y2 = list(map(int, readline().split()))
    if x1 == x2 or y1 == y2:
        Ans[qu] = abs(x1 - x2) + abs(y1 - y2)
    else:
        Ans[qu] = abs(x1 - x2) + abs(y1 - y2) + 2

print('\n'.join(map(str, Ans)))
