def solution(string, ending):
    numbs = len(ending)
    if numbs == 0:
        return True
    elif string[-numbs:] == ending:
        return True
    else:
        return False
