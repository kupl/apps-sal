def solve(s):

    q = ''.join(reversed(s.replace(' ', '')))
    arr = []
    c = 0
    for i in s:
        if i == ' ':
            arr.append(' ')

        else:
            arr.append(q[c])
            c += 1
    return(''.join(arr))
