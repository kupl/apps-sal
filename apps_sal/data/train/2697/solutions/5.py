def solution(s):
    st = ''
    for c in s:
        if c.upper() == c:
            st += ' ' + c
        else:
            st += c
    return st
