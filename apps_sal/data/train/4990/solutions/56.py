def solution(string, ending):
    if ending == "":
        return True
    else:
        return ending in string and ending[-1] == string[-1]
