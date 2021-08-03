def solution(a, b):
    if(len(a) < len(b)):
        result = a + b + a
        return result
    else:
        result = b + a + b
        return result
