def solution(a, b):
    return '{0}{1}{0}'.format(a if len(a) < len(b) else b, a if len(a) > len(b) else b)

