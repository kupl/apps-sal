def solution(a, b):
    if a.isdigit() and b.isdigit():
        return b+a+b if a > b else a+b+a
    else:
        return b+a+b if len(a) > len(b) else a+b+a
        

