def solve():
    s = input().strip()
    i = 0
    j = len(s) - 1
    a = ''
    b = ''
    while i <= j:
        if s[i] != s[j]:
            a = s[:i] + s[i + 1:]
            b = s[:j] + s[j + 1:]
            break
        i += 1
        j -= 1
    if a == a[::-1] or b == b[::-1]:
        print('YES')
    else:
        print('NO')


test = int(input())
for _ in range(test):
    solve()
