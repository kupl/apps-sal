def solution(string, ending):
    l1 = len(string)
    l2 = len(ending)
    l3 = int(l1 - l2)
    l4 = string[l3:]
    if ending == l4:
        return True
    else:
        return False
