def solution(a, b):
    if len(str(a)) < len(str(b)):
        return '{}{}{}'.format(a,b,a)
    else:
        return '{}{}{}'.format(b,a,b)

