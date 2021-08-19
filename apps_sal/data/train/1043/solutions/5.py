n = int(input())
(l, dictonary) = ([], [])
for i in range(n):
    (listSize, numOfDict) = map(int, input().split())
    listOfelement = list(map(str, input().split()))
    for i in range(numOfDict):
        dictonary += list(map(str, input().split()))
    for ele in listOfelement:
        if ele in dictonary:
            l.append('YES')
        else:
            l.append('NO')
    for out in l:
        print(out, end=' ')
    print()
    (dictonary, l) = ([], [])
