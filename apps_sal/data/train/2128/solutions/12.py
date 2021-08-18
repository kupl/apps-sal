n, v = int(input()), list(map(int, input().split()))

ans = 0
r = 0

for i in v:
    if i == 1:
        r += 1
    else:
        ans += r

print(ans)
