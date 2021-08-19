def solve(s):
    st = ''
    a = 0
    arr = []
    for i in s[::-1]:
        if i != ' ':
            st += i
    for j in s:
        if j != ' ':
            a += 1
        elif j == ' ':
            arr.append(a)
            a += 1
    for k in arr:
        st += ' '
        st = st[0:k] + ' ' + st[k:-1]
    return st
