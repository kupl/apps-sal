def solution(string):
    aux = ''
    for i in range(len(string)):
        aux += string[len(string) - i - 1]
    return aux
