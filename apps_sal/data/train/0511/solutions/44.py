n = int(input())
a = list(map(int, input().split()))
s = a[0]
for i in a[1:]:
    s ^= i
ans = ''
for i in a:
    x = s ^ i
    ans += str(x)
    ans += ' '
print(ans[:-1])
