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
    for a, b in finalList:
        if len(test) == 0:
            test.append(b)
            name.append(a)
        else:
            if b in test:
                name.append(a)
                name.sort()
                name = [name[0]]
            else:
                break
    print(name[0])
