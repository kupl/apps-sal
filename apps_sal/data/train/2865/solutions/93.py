def solution(string):
    forwardCharArr = list(string)
    backCharArr = []
    for i in range(len(string) - 1, -1, -1):
        backCharArr.append(forwardCharArr[i])
    reverseWord = ''.join(backCharArr)
    return reverseWord
