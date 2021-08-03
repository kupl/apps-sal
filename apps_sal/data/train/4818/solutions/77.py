def solution(a, b):
    if len(a) > len(b):
        return ''.join([b, a, b])
    elif len(b) > len(a):
        return ''.join([a, b, a])
    else:
        return None
