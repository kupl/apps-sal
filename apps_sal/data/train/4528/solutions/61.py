def my_languages(results):
    resultList = []
    sortedDict = {}

    sortList = sorted(list(results.items()), key=lambda x: x[1], reverse=True)

    for i in sortList:
        print((i[0], i[1]))
        sortedDict.update({i[0]: i[1]})

    print(sortedDict)

    for i in sortedDict:
        if results[i] >= 60:
            resultList.append(i)
        else:
            pass
    return resultList

# for i in sort_orders:
#   print(i[0], i[1])
