def solution(a, b):
    short = b if len(a) > len(b) else a
    long = a if len(a) > len(b) else b
    return f'{short}{long}{short}'
