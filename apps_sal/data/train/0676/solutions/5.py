testCase = int(input())
for _ in range(testCase):
    numBoys = int(input())
    finalList = []
    boysList = [i for i in input().split()]
    boysList.sort()
    while len(boysList) != 0:
        name = boysList[0]
        coun = boysList.count(boysList[0])
        finalList.append([boysList[0], coun])
        while name in boysList:
            boysList.remove(name)

    finalList.sort(key=lambda x: x[1])
    finalList.reverse()
    test = []
    name = []
    for z in finalList:
        if len(test) == 0:
            test.append(z[1])
            name.append(z[0])
        else:
            if z[1] in test:
                name.append(z[0])
            else:
                break
    if len(name) > 1:
        name.sort()
        print(name[0])
    else:
        print(name[0])
