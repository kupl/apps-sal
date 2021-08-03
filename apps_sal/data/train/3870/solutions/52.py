def solve(s):
    ss = s.replace(' ', '')[::-1]
    for i in range(len(s)):
        if s[i] == ' ':
            ss = ss[:i] + ' ' + ss[i:]
    return ss
