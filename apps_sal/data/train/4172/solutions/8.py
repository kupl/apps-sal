def dellall(s):
    n = 0
    while True:
        if n == len(s) - 1 or len(s) == 0:
            return True
        if s[n] == '(' and s[n + 1] == ')':
            del s[n]
            del s[n]
            n = 0
        else:
            n += 1


def solve(s):
    s = list(s)
    count = 0
    if len(s) % 2 != 0:
        return -1
    dellall(s)
    while len(s) != 0:
        n = 0
        if s[n] == '(' and s[n + 1] == ')':
            del s[n]
            del s[n]
        elif s[n] == ')' and s[n + 1] == '(':
            s[n] = '('
            s[n + 1] = ')'
            count += 2
        elif s[n] == '(' and s[n + 1] == '(':
            s[n + 1] = ')'
            count += 1
        elif s[n] == ')' and s[n + 1] == ')':
            s[n] = '('
            count += 1
    return count
