def solution(n, d):
    return [int(c) for c in str(n)[-d:]] if d > 0 else []
