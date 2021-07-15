def solution(string, ending):
    return string[-len(ending):] == ending if ending is not '' else True
