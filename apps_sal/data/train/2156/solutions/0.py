n = int(input())
ans = 'YES\n'
for i in range(n):
    (x1, y1, x2, y2) = map(int, input().split())
    res = (x1 & 1) * 2 + (y1 & 1) + 1
    ans += str(res) + '\n'
print(ans)
