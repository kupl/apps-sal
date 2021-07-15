def solution(a, b):
    if a is None and b is None: return a
    elif b is None: return a
    elif a is None: return b
    else: 
        a_len = len(a)
        b_len = len(b)
        if a_len >= b_len:
            return b + a + b
        else:
            return a + b + a
