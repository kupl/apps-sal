def solution(s, e):
    return not e or s[-len(e):] == e
