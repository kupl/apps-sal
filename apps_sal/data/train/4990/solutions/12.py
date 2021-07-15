def solution(string, ending):
    return string[len(string)-len(ending):len(string)] == ending

