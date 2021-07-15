def solution (a, b):
    return ''.join(a + b + a if len(a) < len(b) else b + a + b)

#def solution(a, b):
#    return ''.join(a + b + a if len(a) < len(b) else b + a + b)

