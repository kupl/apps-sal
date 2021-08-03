from sys import stdin, stdout
k = 20


def findAllStrings(s):
    n = len(s)
    sdict = {}
    for i in range(1, k + 1):
        sdict[i] = set()
        for x in range(n - i + 1):
            sdict[i].add(s[x:x + i])
    return sdict


n = int(stdin.readline().rstrip())
strdict = []
stringend = []
stringbegin = []
for i in range(n):
    s = stdin.readline().rstrip()
    strdict.append(findAllStrings(s))
    if len(s) < k:
        stringend.append(s)
        stringbegin.append(s)
    else:
        stringend.append(s[-20:])
        stringbegin.append(s[:20])
m = int(stdin.readline().rstrip())
for _ in range(m):
    a, b = list(map(int, stdin.readline().rstrip().split()))
    a -= 1
    b -= 1
    sdict1 = findAllStrings(stringend[a] + stringbegin[b])
    sdict2 = strdict[a]
    sdict3 = strdict[b]
    sdict = {}
    for i in range(1, k + 1):
        sdict[i] = sdict1[i] | sdict2[i] | sdict3[i]
    strdict.append(sdict)
    for i in range(1, k + 1):
        if len(sdict[i]) != 2**i:
            print(i - 1)
            break
    if len(stringbegin[a]) < k and len(stringbegin[a]) + len(stringbegin[b]) < k:
        stringbegin.append(stringbegin[a] + stringbegin[b])
    elif len(stringbegin[a]) < k:
        s = stringbegin[a] + stringbegin[b]
        stringbegin.append(s[:k])
    else:
        stringbegin.append(stringbegin[a])

    if len(stringend[b]) < k and len(stringend[a]) + len(stringend[b]) < k:
        stringend.append(stringend[a] + stringend[b])
    elif len(stringend[b]) < k:
        s = stringend[a] + stringend[b]
        stringend.append(s[-k:])
    else:
        stringend.append(stringend[b])
