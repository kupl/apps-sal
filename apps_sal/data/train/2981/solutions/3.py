def solution(n,d):
    return list(map(int, list(str(n)[-d:]))) if d > 0 else []
