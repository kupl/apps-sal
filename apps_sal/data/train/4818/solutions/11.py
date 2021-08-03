def solution(a: str, b: str) -> str:
    short, int = sorted((a, b), key=len)
    return f"{short}{long}{short}"
