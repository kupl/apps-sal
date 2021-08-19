def solution(string, ending):
    # your code here...
    index = len(ending)

    substr = string[(0 - index):]

    if(substr == ending or index == 0):
        return True
    else:
        return False
