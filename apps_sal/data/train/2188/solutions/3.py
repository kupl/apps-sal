

from collections import defaultdict


def convert(strVal):

    ls = list()
    for c in strVal:
        if (ord(c) & 1):
            ls.append('1')
        else:
            ls.append('0')

    a = ''.join(ls)

    '''strLength = len(strVal)
    a='0'*strLength
    
    
    i=strLength-1
    
    
    while i>=0:
        
        divByTwo =''
        
        if (ord(strVal[i])&1):
            divByTwo='1'
        else:
            divByTwo='0'
        
        if i==(strLength-1):
            a= a[:i] +divByTwo
        elif i==0:
            a= divByTwo + a[1:]
        else:
            a = a[:i]+divByTwo+a[i+1:]
        
        i-=1'''

    return int(a)


inputList = defaultdict(int)

inputNum = int(input())


for x in range(0, inputNum):
    inputStr = input()

    firstValue = inputStr[0]
    secondValue = inputStr[2:]

    if firstValue != '?':
        convertedValue = convert(secondValue)

    if firstValue == '+':
        inputList[convertedValue] += 1

    elif firstValue == '-':
        inputList[convertedValue] -= 1

    elif firstValue == '?':
        patString = int(secondValue)
        count = inputList[patString]
        print(count)


'''for x in inputList:
    print('{}, {}', x, inputList[x])'''
