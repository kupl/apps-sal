def solution(a, b):
    short, int = sorted((a, b), key=len)
    return short + int + short

