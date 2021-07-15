gans = []
for _ in range(int(input())):
    s = list(input())
    n = len(s)
    cur = 0
    ans = n
    for i in range(n - 1, -1, -1):
        if s[i] == 'B':
            cur += 1
        else:
            if cur > 0:
                cur -= 1
                ans -= 2
    ans -= cur - cur % 2
    gans.append(ans)
print('\n'.join(map(str, gans)))
        

