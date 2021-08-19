def super_size(n):
    digitList = list(str(n))
    if len(digitList) == 1:
        return n
    else:
        digitList.sort()
        digitList.reverse()
    largestValue = ''
    for digit in digitList:
        largestValue += digit
    return int(largestValue)
