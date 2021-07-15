def solution(string):
    return ''.join((char if char.islower() else ' ' + char) for char in string)
