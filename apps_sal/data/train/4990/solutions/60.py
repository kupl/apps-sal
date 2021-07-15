def solution(string, ending):
    s = string
    e = ending
    counter = len(e)
    
    if e in s and s[-counter:] == e:
        return True
    if counter == 0:
        return True
    else:
        return False

