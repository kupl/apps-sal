def solution(a, b):
    la, lb = len(a), len(b)
    return f"{(a, b)[lb<la]}{(a, b)[lb>la]}{(a, b)[lb<la]}"

