def solution(string):
    phrase = ''
    index = len(string) - 1
    for x in string:
        x = string[index]
        phrase += x
        index = index - 1
    return phrase
