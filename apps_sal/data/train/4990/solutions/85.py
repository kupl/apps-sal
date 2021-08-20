def solution(string, ending):
    if string[int(len(ending) * -1):] == ending:
        return True
    elif ending == '':
        return True
    else:
        return False
