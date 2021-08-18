import sys
input = sys.stdin.readline

n, d, m = map(int, input().split())
a = list(map(int, input().split()))

up = []
down = []
for i in range(n):
    if a[i] > m:
        up.append(a[i])
    else:
        down.append(a[i])

up = sorted(up)
down = sorted(down)

if not up:
    print(sum(down))
    return

ans = 0
ans += up.pop()
lap, rem = divmod((n - 1), (d + 1))
for i in range(rem):
    if not down:
        break
    else:
        ans += down.pop()

matome = []
while down:
    tmp = 0
    for _ in range(d + 1):
        if down:
            tmp += down.pop()
    matome.append(tmp)

matome = sorted(matome + up, reverse=True)
ans += sum(matome[0:min(lap, len(matome))])

print(ans)
