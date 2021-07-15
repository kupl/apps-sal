def solution(string):
    new_string = ""
    length = len(string)
    for i in range(0, length):
        new_string += string[length-1-i]
    return new_string
