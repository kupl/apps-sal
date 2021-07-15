def solution(a, b):
    print((len(a)))

    if len(a) > len(b):
        answer = b + a + b
        return answer
    else:
        answer = a + b + a
        return answer

