def solution(a='', b=''):
    return f'{a}{b}{a}' if len(b) > len(a) else f'{b}{a}{b}'
    

