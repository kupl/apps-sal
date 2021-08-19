def solution(string, ending):
    f = len(ending)
    h = [i for i in ending]
    r = []
    for i in string:
        r.append(i)
    r = r[-f:]
    if r == h:
        return True
    elif h == []:
        return True
    else:
        return False
