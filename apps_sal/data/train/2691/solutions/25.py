def solve(s):
    for i in s:
        if i not in '0123456789':
            s = s.replace(i,' ')
    s = s.split()
    return sorted([int(i) for i in s])[-1]
