def maxnum(s, k):
    l = len(s)
    if l == 0 or k == 0:
        return s
    if l == 1:
        return '9'
    if s[0] != '9':
        s = '9' + s[1:]
        k -= 1
    i = 1
    while k > 0 and i < l:
        if s[i] != '9':
            s = s[:i] + '9' + s[i + 1:]
            k -= 1
        i += 1
    return s


(n, k) = list(map(int, input().split()))
s = f'{n}'
print(maxnum(s, k))
