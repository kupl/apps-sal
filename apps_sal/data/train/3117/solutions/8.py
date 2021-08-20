def solve(s):
    for x in s:
        if x not in 'aeiou':
            s = s.replace(x, ' ')
    s = s.split()
    a = [len(x) for x in s]
    return max(a)
