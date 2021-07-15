def braces_status(s):
    l = []
    d = {'(': ')', '{': '}', '[': ']'}
    for x in s:
        if x in '({[':
            l.append(d[x])
        elif x in ')}]':
            if not l or not x == l.pop():
                return 0
    return not l
