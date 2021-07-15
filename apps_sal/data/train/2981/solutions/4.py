def solution(n,d):
    return [int(s) for s in str(n)[-d:]] if d > 0 else []
