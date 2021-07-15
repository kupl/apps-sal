n = int(input())
num = [0] * (2 * (10 ** 6) + 1)
for i in map(int, input().split()):
    num[i] += 1
ans = 0
for i in range(2 * (10 ** 6)):
    num[i + 1] += num[i] // 2
    ans += num[i] % 2
print(ans + num[-1] % 2)
