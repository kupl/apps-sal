n = int(input())
mainlist = []
choppedlist = []
for i in range(0, n):
    mainlist.append(input().split())

for i in range(0, n):
    mainlist[i][0] = int(mainlist[i][0])
    mainlist[i][1] = int(mainlist[i][1])

# print('typeis ',type(mainlist[0][0]))


def checkifpossible(mainlist, sublist, right, pos):
    # print('sublist is ', sublist)
    # print('mainlist is ', mainlist)
    returncode = True

    if right:
        for i in range(pos + 1, n):
            # print('at right value of m and s are ', mainlist[i][0], ' ',                 sublist[1])
            if mainlist[i][0] <= sublist[1]:
                returncode = False
    else:
        for i in range(0, pos):
            # print('value of m and s are ', mainlist[i][0], ' ', sublist[0])
            if mainlist[i][0] >= sublist[0]:
                # print('setting to False')
                returncode = False
    for j in range(0, len(choppedlist)):
        if choppedlist[j][1] >= sublist[0] and not right:
            # print('overlapping chopped list')
            returncode = False

    return returncode


def choptreetoright(mainlist, pos):
    nonlocal choppedlist
    sublist = []
    sublist.append(mainlist[pos][0])
    sublist.append(mainlist[pos][0] + mainlist[pos][1])
    right = True

    if checkifpossible(mainlist, sublist, right, pos) == True:
        choppedlist.append(sublist)
        return True
    else:
        return False


def choptreetoleft(mainlist, pos):
    nonlocal choppedlist
    sublist = []
    sublist.append(mainlist[pos][0] - mainlist[pos][1])
    sublist.append(mainlist[pos][0])
    right = False
    if checkifpossible(mainlist, sublist, right, pos) == True:
        choppedlist.append(sublist)
        return True
    else:
        return False


if n >= 2:
    counter = 2
elif n == 1:
    counter = 1
else:
    counter = 0

for i in range(1, n - 1):
    # print('calling left with i ', i)
    if choptreetoleft(mainlist, i):
        counter = counter + 1
        continue
    # print('calling right with i ', i)
    if choptreetoright(mainlist, i):
        counter = counter + 1

# print('chopped list ', choppedlist)
print(counter)
