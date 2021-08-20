n = int(input())
ans = []
for i in range(0, 90):
    x = n - i
    if x <= 0:
        continue
    ds = 0
    s = str(x)
    for c in s:
        ds += ord(c) - ord('0')
    if ds == i:
        ans.append(x)
ans = sorted(ans)
print(len(ans))
print(' '.join(map(str, ans)))
