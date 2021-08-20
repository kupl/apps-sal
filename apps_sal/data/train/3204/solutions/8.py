def Guess_it(n, m):
    if n == 0:
        return [[]]
    arrayStorage = {0: [], 1: [], 2: [], 3: [[0, 0, 1]], 4: [[0, 1, 0]], 5: [[1, 0, 0]]}
    if m in arrayStorage:
        return arrayStorage[m]
    for i in range(6, m + 1):
        arrayStorage[i] = []
        arraysTemp = arrayStorage[i - 3]
        for array in arraysTemp:
            if sum(array) < n:
                elemToAdd = [array[0], array[1], array[2] + 1]
                if elemToAdd not in arrayStorage[i]:
                    arrayStorage[i].append(elemToAdd)
        arraysTemp = arrayStorage[i - 4]
        for array in arraysTemp:
            if sum(array) < n:
                elemToAdd = [array[0], array[1] + 1, array[2]]
                if elemToAdd not in arrayStorage[i]:
                    arrayStorage[i].append(elemToAdd)
        arraysTemp = arrayStorage[i - 5]
        for array in arraysTemp:
            if sum(array) < n:
                elemToAdd = [array[0] + 1, array[1], array[2]]
                if elemToAdd not in arrayStorage[i]:
                    arrayStorage[i].append(elemToAdd)
    resultArray = []
    for array in arrayStorage[m]:
        if sum(array) == n:
            resultArray.append(array)
    return sorted(resultArray, key=lambda x: x[0])
