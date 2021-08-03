def solution(n, d):
    return [int(i) for i in str(n)][::-1][:d][::-1] if d > 0 else []
