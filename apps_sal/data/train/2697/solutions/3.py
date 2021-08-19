def solution(s):
    newStr = ''
    for letter in s:
        if letter.isupper():
            newStr += ' '
        newStr += letter
    return newStr
