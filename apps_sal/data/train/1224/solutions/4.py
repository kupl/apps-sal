def findRemainigSum(start, digitSum, upTo):
    sum = 0
    currSum = findSumOfDigits(start)
    for i in range(0, upTo):
        sum += findSumOfDigits(currSum)
        currSum = findSumOfDigits(currSum + digitSum)
    return sum


def findSumOfDigits(num):
    if(num % 9 == 0) and (num != 0):
        return 9
    else:
        return num % 9


t = int(input())
while(t):
    inputString = input()
    inputList = inputString.split()
    a = int(inputList[0])
    d = int(inputList[1])
    l = int(inputList[2])
    r = int(inputList[3])
    sum = 0
    diff = r - l + 1
    lDigitSum = findSumOfDigits(a + (l - 1) * d)
    dDigitSum = findSumOfDigits(d)
    if(dDigitSum == 9 or dDigitSum == 0):
        sum = lDigitSum * diff

    else:
        if(dDigitSum == 3 or dDigitSum == 6):
            n1 = lDigitSum
            n2 = findSumOfDigits(lDigitSum + dDigitSum)
            n3 = findSumOfDigits(n2 + dDigitSum)
            sum = (int(diff / 3)) * (n1 + n2 + n3) + findRemainigSum(lDigitSum, dDigitSum, diff % 3)
        else:
            sum = (int(diff / 9)) * 45 + findRemainigSum(lDigitSum, dDigitSum, diff % 9)
    print(sum)
    t -= 1
