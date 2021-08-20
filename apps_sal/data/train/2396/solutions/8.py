import sys
inp = sys.stdin.read().split()
ii = 0
t = int(inp[0])
ii += 1
for _ in range(t):
    n = int(inp[ii])
    ii += 1
    s = inp[ii]
    ii += 1
    if n == 1:
        if 'a' in s:
            print(0)
        else:
            print(1)
        continue
    stack = [[0, n, ord('a'), 0]]
    ans = n
    while stack:
        (l, r, c, cost) = stack[-1]
        stack.pop()
        if r - l == 1:
            if chr(c) in s[l:r]:
                ans = min(ans, cost)
            else:
                ans = min(ans, cost + 1)
            continue
        mid = (l + r) // 2
        stack.append([l, mid, c + 1, r - mid + cost - s[mid:r].count(chr(c))])
        stack.append([mid, r, c + 1, mid - l + cost - s[l:mid].count(chr(c))])
    print(ans)
