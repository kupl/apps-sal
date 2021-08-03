def cal(s):
    res = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                res ^= 1
    return res


def solve():
    [n, s, t] = [input(), input(), input()]
    if(sorted(s) != sorted(t)):
        print('NO')
        return
    for i in range(26):
        if s.count(chr(ord('a') + i)) > 1:
            print('YES')
            return
    print(['NO', 'YES'][cal(s) == cal(t)])


for i in range(int(input())):
    solve()
