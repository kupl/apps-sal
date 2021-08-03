def solution(string, ending):
    ns = len(string)
    ne = len(ending)
    if(ne == 0):
        return True
    else:
        if(string[-ne::] == ending):
            return True
        else:
            return False
