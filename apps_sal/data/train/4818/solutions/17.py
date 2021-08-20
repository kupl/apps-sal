def solution(a, b):
    return (a + b + a, b + a + b)[len(a) > len(b)]
