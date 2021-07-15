def solution(a, b):
    try:
        x = int(a, b)
    except:
        return a+b+a if len(b) > len(a) else b+a+b
    else:
        return a+b+a if b > a else b+a+b


