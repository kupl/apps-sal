def solution(a, b):
    if len(a) > len(b):
        return "{0}{1}{0}".format(b,a)
    else:
        return "{0}{1}{0}".format(a,b)
        

