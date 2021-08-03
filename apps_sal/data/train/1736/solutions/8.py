def isZeros(nStr): return sum(map(int, list(nStr))) == int(nStr[0])


def isAll(nStr): return nStr == nStr[0] * len(nStr)
def isInc(nStr): return nStr in "9876543210 1234567890"
def isPalin(nStr): return nStr == nStr[::-1]


def is_interesting(number, awesome_phrases):
    for i in range(3):
        nStr = str(number + i)
        if int(nStr) > 99 and (isZeros(nStr) or isAll(nStr) or isInc(nStr) or isPalin(nStr) or int(nStr) in awesome_phrases):
            return {0: 2, 1: 1, 2: 1}[i]
    return 0
