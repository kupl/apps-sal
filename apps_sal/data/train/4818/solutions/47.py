def solution(a, b):
    if len(a)>len(b):
        result=b+a+b
    elif len(b)>len(a):
        result=a+b+a
    else:
        result=""
    return result

