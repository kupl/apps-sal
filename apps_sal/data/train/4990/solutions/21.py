def solution(string, ending):
    return string[len(ending) * -1:] == ending or ending == ''
