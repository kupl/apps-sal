def solution(a, b):
    if len(a) > len(b):
        return str(f'{b}{a}{b}')
    else:
        return str(f'{a}{b}{a}')
