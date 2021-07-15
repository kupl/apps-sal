def solution(string):
    rev = ''
    for i in range(len(string)):
        rev += string[len(string) - i - 1]
    return rev
