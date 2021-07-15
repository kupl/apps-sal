def solution(a, b):
    shortest, longest = (a, b) if len(a) < len(b) else (b, a)
    return shortest + longest + shortest

