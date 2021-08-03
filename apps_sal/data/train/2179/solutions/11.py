a, b, c = list(map(int, input().split(' ')))
n = int(input())
ans = 0
x = list(map(int, input().split(' ')))
for i in x:
    if i > b and i < c:
        ans += 1
print(ans)
