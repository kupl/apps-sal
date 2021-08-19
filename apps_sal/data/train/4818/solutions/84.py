def solution(a, b):
    return '%s%s%s' % (a, b, a) if len(a) < len(b) else '%s%s%s' % (b, a, b)
