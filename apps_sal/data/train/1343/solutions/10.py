from collections import Counter


def is_spcl(s, n):
    return s[:n // 2] == s[n // 2:]


for _ in range(int(input())):
    s = input()
    n = len(s)
    if len(s) == 1:
        print('NO')
        continue
    if s[0:n // 2] == s[n // 2:]:
        print('YES')
        continue
    f = 0
    for i in range(0, n):
        if is_spcl(s[0:i] + s[i + 1:], n - 1):
            f = 1
            break
    print('YES' if f else 'NO')
