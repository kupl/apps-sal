def solution(string):
    stringReversal = []
    somaReverseString = ''
    for i in range(len(string)):
        migratingCharacter = string.replace(string[i], string[-i - 1])
        stringReversal.append(migratingCharacter[i])
        string.replace(string[i], string[-i - 1])
    for i in stringReversal:
        somaReverseString += i
    return somaReverseString


def solution(string):
    strings = []
    soma = ''
    stringLengthRange = list(range(len(string)))
    for i in stringLengthRange:
        strings.append(string[-i - 1])
    for i in strings:
        soma += i
    return soma


def solution(string):
    return string[::-1]
