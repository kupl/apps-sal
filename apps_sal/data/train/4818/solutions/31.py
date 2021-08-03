def solution(a, b):
    if type(a) == int:

        if a < b:
            return a + b + a
        elif a > b:
            return b + a + b

    if type(a) == str:

        if len(a) < len(b):
            return a + b + a
        elif len(a) > len(b):
            return b + a + b
