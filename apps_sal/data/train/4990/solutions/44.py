def solution(string, ending):
    newEnding = ending[::-1]
    newString = string[::-1]
    stringCount = 0
    print(newString, newEnding)
    for letters in newEnding:
        if stringCount < len(newString):
            print(stringCount)
            if letters != newString[stringCount]:
                return False
            stringCount += 1
        else:
            return False
    return True
