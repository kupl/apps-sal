MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


s = input()
n = len(s)
ans = [0] * (n + 1)
l = n
r = 1
stone = 1
for i in s:
    if i == 'l':
        ans[l] = stone
        l -= 1
    if i == 'r':
        ans[r] = stone
        r += 1
    stone += 1
# print(ans)
for i in ans[1:]:
    print(i)
