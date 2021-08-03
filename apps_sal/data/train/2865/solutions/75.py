def solution(string):
    index = len(string) - 1
    str = ""
    while index >= 0:
        str = str + string[index]
        index = index - 1
    return str
