def solution(a, b):
    return f'{b}{a}{b}' if len(a) > len(b) else f'{a}{b}{a}'
