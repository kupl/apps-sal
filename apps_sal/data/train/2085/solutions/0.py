from sys import stdin, stdout

K = 20


def findAllStrings(s):
    n = len(s)
    sDict = {}
    for i in range(1, K + 1):
        sDict[i] = set()
        for x in range(n - i + 1):
            sDict[i].add(s[x:x + i])
    return sDict


n = int(stdin.readline().rstrip())
stringDicts = []
stringEnd = []
stringBegin = []

for i in range(n):
    s = stdin.readline().rstrip()
    stringDicts.append(findAllStrings(s))
    if len(s) < K:
        stringEnd.append(s)
        stringBegin.append(s)
    else:
        stringEnd.append(s[-20:])
        stringBegin.append(s[:20])

m = int(stdin.readline().rstrip())

for _ in range(m):
    a, b = list(map(int, stdin.readline().rstrip().split()))
    a -= 1
    b -= 1

    sDict1 = findAllStrings(stringEnd[a] + stringBegin[b])
    sDict2 = stringDicts[a]
    sDict3 = stringDicts[b]
    sDict = {}
    for i in range(1, K + 1):
        sDict[i] = sDict1[i] | sDict2[i] | sDict3[i]
    stringDicts.append(sDict)
    for i in range(1, K + 1):
        if len(sDict[i]) != 2**i:
            print(i - 1)
            break

    if len(stringBegin[a]) < K and len(stringBegin[a]) + len(stringBegin[b]) < K:
        stringBegin.append(stringBegin[a] + stringBegin[b])
    elif len(stringBegin[a]) < K:
        s = stringBegin[a] + stringBegin[b]
        stringBegin.append(s[:K])
    else:
        stringBegin.append(stringBegin[a])

    if len(stringEnd[b]) < K and len(stringEnd[a]) + len(stringEnd[b]) < K:
        stringEnd.append(stringEnd[a] + stringEnd[b])
    elif len(stringEnd[b]) < K:
        s = stringEnd[a] + stringEnd[b]
        stringEnd.append(s[-K:])
    else:
        stringEnd.append(stringEnd[b])
