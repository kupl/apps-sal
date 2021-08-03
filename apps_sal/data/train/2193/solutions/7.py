n = int(input())
a = []
s = sum(list(map(int, input().split())))
ans = 1
for i in range(n - 1):
    x = sum(list(map(int, input().split())))
    if x > s:
        ans += 1

print(ans)
