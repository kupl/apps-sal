def solution(n, d):
    if d <= 0:
        return []
    else:
        return [int(i) for i in str(n)][-d:]
