def near_flatten(A):
    s = str(A)[1:-1]
    while '[[' in s:
        s = s.replace('[[', '[')
    while ']]' in s:
        s = s.replace(']]', ']')
    return sorted(list(map(int, x.split(',')))for x in s[1:-1].split('], ['))
