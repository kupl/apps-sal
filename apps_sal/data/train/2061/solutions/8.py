def solve(*args):
    sx = sum(args[::2])
    sy = sum(args[1::2])
    dx = sx - sx // 3 - 1
    dy = sy - sy // 3 - 1
    ans = max(abs(dx), abs(dy))
    if sx == sy and sx // 3 != 0:
        ans += 1
    return ans


t = int(input())
for i in range(t):
    print((solve(*list(map(int, input().split())))))
