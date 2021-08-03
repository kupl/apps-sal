def solution(string, ending):
    end = string[len(string) - len(ending):len(string)]
    return end == ending
