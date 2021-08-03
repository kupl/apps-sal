def solution(string, ending):
    lenEnd = len(ending)

    if (string[-lenEnd:] == ending) or (ending == ''):
        return True
    else:
        return False
