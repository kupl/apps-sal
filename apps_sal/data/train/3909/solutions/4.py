def is_keith_number(n):
    s = list(map(int, str(n)))
    l = len(s)
    while s[-1] < n:
        s.append(sum(s[-l:]))
    return len(s) - l if n in s else False
