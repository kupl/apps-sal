def solution(string):
    newstring = ''
    letter = len(string) - 1
    for x in string:
        x = string[letter]
        newstring = newstring + x
        letter = letter - 1
    return newstring
