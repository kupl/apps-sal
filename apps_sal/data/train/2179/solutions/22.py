[a, b, c] = list(map(int, input().split()))
n = int(input())
notes = list(map(int, input().split()))
ans = 0
for i in notes:
    if i > b and i < c:
        ans += 1
print(ans)
