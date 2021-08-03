def GregAndArray():
    lenArray, numOperations, numQueries = map(int, input().split())
    initialArray = list(map(int, input().split()))

    instructions = [list(map(int, input().split())) for _ in range(numOperations)]

    modifiedArray = [0 for _ in range(lenArray + 1)]
    queries = [0 for _ in range(numOperations + 1)]

    for _ in range(numQueries):
        x, y = map(int, input().split())

        queries[x - 1] += 1
        queries[y] -= 1

    temp = 0
    for i in range(numOperations):
        temp += queries[i]
        modifiedArray[instructions[i][0] - 1] += temp * instructions[i][2]
        modifiedArray[instructions[i][1]] -= temp * instructions[i][2]

    temp = 0
    toReturn = ""
    for i in range(lenArray):
        temp += modifiedArray[i]
        toReturn += (str(temp + initialArray[i]) + " ")

    print(toReturn)


GregAndArray()
