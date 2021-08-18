def solution(string, ending):
    return string[-len(ending):] == ending or ending == ""
