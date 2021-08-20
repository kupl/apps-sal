def solution(string):
    if len(string) <= 1:
        return string
    else:
        string = string[::-1]
        return string
