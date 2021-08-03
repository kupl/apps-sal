n = int(input())
a = [int(x) for x in input().split()]
ans = 0
r = 0
for x in a:
    if x == 1:
        r += 1
    else:
        ans += r
print(ans)
