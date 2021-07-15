def solution(string):
    new_str = ""
    lnum = len(string)
    for i in range(lnum):
        new_str = new_str + string[lnum-i-1]
    return new_str
