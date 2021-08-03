def solve(s):
    reversed = list(''.join(s.split())[::-1])
    for i in range(len(s)):
        if s[i] == ' ':
            reversed.insert(i, ' ')
    return ''.join(reversed)
