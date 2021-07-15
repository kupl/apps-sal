def solution(string):
    aux = []
    for i in range(len(string)):
        aux.append(string[len(string) - i - 1])
    return ''.join(aux)
