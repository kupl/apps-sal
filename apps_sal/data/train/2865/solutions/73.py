def solution(string):
    pass
    index = len(string)
    rev = ""
    while index > 0 :
        rev += string[index - 1]
        index = index - 1
    return (rev)
