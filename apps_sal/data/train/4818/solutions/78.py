def solution(a, b):
    return a+b+a if len(a+b+a) < len(b+a+b) else b+a+b
