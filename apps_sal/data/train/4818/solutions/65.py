def solution(a='', b=''):
    if len(a) > len(b):
        return f'{b}{a}{b}'
    elif len(a) < len(b):
        return f'{a}{b}{a}'
