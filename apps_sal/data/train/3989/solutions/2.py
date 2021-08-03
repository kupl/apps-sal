def solution(n):
    return sum(f * c * (c + 1) for f, c in ((f, (n - 1) // abs(f)) for f in (3, 5, -15))) // 2
