def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    elif len(a) < len(b):
        return a + b + a


print(solution('123', '34'))
