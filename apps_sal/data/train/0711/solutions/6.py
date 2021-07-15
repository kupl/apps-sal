# cook your dish here
def letterNo(c):
    if i == '?':
        return 26
    return ord(c) - 97
for _ in range(int(input())):
    s = input().strip()
    mask = 0
    for i in s:
        if i != '?':
            mask ^= (1 << letterNo(i))
    d = {}
    x = 0
    d[0] = 1
    ans = 0
    for i in s:
        x ^= (1 << letterNo(i))
        ans += d.get(x^mask, 0)
        for j in range(26):
            ans += d.get(x^(1 << 26)^(1 << j)^mask, 0)
        d[x] = d.get(x, 0) + 1
    print(ans)

