
testCase = int(input())
for _ in range(testCase):
    numBoys = int(input())
    finalList = []
    boysList = [i for i in input().split()]
    boysList.sort()
    while len(boysList) != 0:
        coun = boysList.count(boysList[0])
        finalList.append([boysList[0], coun])
        for _ in range(coun):
            boysList.remove(boysList[0])

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
                name.sort()
                name = [name[0]]
            else:
                break
    print(name[0])
