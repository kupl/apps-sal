from collections import defaultdict


def convert(strVal):
    ls = list()
    for c in strVal:
        if ord(c) & 1:
            ls.append('1')
        else:
            ls.append('0')
    a = ''.join(ls)
    "strLength = len(strVal)\n    a='0'*strLength\n    \n    \n    i=strLength-1\n    \n    \n    while i>=0:\n        \n        divByTwo =''\n        \n        if (ord(strVal[i])&1):\n            divByTwo='1'\n        else:\n            divByTwo='0'\n        \n        if i==(strLength-1):\n            a= a[:i] +divByTwo\n        elif i==0:\n            a= divByTwo + a[1:]\n        else:\n            a = a[:i]+divByTwo+a[i+1:]\n        \n        i-=1"
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
"for x in inputList:\n    print('{}, {}', x, inputList[x])"
