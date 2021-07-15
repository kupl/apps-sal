def solution(a, b):
    k = ''
    if len(a) < len(b):
        k = ''.join(a) + ''.join(b) + ''.join(a)
    else:
        k = ''.join(b) + ''.join(a) + ''.join(b)
    return k

