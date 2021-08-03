def solution(a, b):
    newString = ''
    if len(a) < len(b):
        return (newString + a + b + a)
    else:
        return (newString + b + a + b)
