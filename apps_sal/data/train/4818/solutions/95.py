def solution(a, b):
    s, l = sorted([a, b], key = len)
    return '{}{}{}'.format(s, l, s)

