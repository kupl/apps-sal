import re


def reverse_words(text):
    wordList = re.findall('\\S+', text)
    spaceList = re.findall('\\s+', text)
    answerList = []
    answerString = ''
    spaceCounter = 0
    for word in wordList:
        answerList.append(word[::-1])
        if spaceCounter < len(spaceList):
            answerList.append(spaceList[spaceCounter])
            spaceCounter += 1
    return answerString.join(answerList)
