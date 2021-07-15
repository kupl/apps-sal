def solution(a, b):
    try:
        if int(a) < int(b):
            return a + b + a
        else:
            return b + a + b 
    except: 
        if len(a) < len(b):
            return a + b + a
        else:
            return b + a + b 
        

