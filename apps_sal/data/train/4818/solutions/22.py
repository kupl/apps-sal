def solution(a: str, b: str) -> str:
    if len(a) < len(b):
        return a + b + a
    return b + a + b

