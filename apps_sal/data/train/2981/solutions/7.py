def solution(n, d):
    return [int(i) for i in str(n)[-d:]] if d > 0 else []
