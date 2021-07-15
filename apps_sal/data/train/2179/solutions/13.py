a, b, c = list(map(int, input().split()))
n = int(input())
x = list(map(int, input().split()))
ans = 0
for i in x:
    if b < i < c:
        ans += 1
print(ans)

