def solution(a, b):
    if(len(a)>len(b)):
        c=(b,a,b)
        return ("".join(c))
    c=(a,b,a)
    return ("".join(c))
