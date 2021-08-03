def solution(n, d):
    return [] if d <= 0 else [int(c) for c in str(n)[-d:]]
