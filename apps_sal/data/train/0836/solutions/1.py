__author__ = 'Hacktivist'

test = int(input())
for testCases in range(test):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    hackmul = 0
    hackIndex = 0
    hackFound = False
    for item in range(len(l)):
        hackVar = l[item] * r[item]
        if hackVar > hackmul:
            hackmul = l[item] * r[item]
            hackIndex = item
            hackVar = 0
        if hackVar == hackmul:
            hackFound = True
    if hackFound:
        print(r.index(max(r)) + 1)
    else:
        print(hackIndex + 1)
