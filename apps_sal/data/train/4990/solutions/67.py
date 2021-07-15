def solution(string, ending):
    if len(ending) != 0:
        if ending[::-1] in string[::-1][:len(ending)]:
            return True
        else:
            return False
    else:
        return True
