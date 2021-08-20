def vert_mirror(strng):
    ans = ''
    sq = strng.split('\n')
    dim = len(sq)
    for i in range(0, dim, 1):
        print(i)
        ans += str(sq[i][::-1]) + '\n'
    return ans.rstrip('\n')


def hor_mirror(strng):
    ans = ''
    sq = strng.split('\n')
    dim = len(sq)
    for i in range(dim, 0, -1):
        ans += str(sq[i - 1]) + '\n'
    return ans.rstrip('\n')


def oper(fct, s):
    return vert_mirror(s) if fct == vert_mirror else hor_mirror(s)
