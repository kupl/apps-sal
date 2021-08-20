(a, b, c) = map(int, input().split())
n = int(input())
s = [int(i) for i in input().split()]
ans = 0
for i in s:
    if i > b and i < c:
        ans += 1
print(ans)
