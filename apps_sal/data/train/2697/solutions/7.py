def solution(s):
    index, string = 0, ""
    for char in s:
        if char.islower():
            string += char
        else:
            string += " " + char
    return string
