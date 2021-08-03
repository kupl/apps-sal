def solution(string, ending):
    if ending is "":
        return True
    ln = len(ending)
    string = string[::-1]
    str = string[:ln]
    return str[::-1] == ending
