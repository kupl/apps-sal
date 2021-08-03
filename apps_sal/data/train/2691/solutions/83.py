def solve(s):
    lst = []
    i = 0
    while len(s) > i:
        if s[i].isdigit():
            lst.append(s[i])
            i += 1
        else:
            lst.append('*')
            i += 1
    lst = ''.join(lst)
    lst = lst.replace('*', ' ')
    lst = lst.split()
    lst = list(map(int, lst))
    return max(lst)
