def solution(a, b):
    if len(a) <= len(b):
        return '{a}{b}{a}'.format(a=a, b=b)
    elif len(a) >= len(b):
        return '{b}{a}{b}'.format(a=a, b=b)
