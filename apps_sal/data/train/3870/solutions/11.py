def solve(s):
    spaceIndex = []
    result = []
    index = 0
    for i in s:
        if i != ' ':
            result.insert(1, i)
        else:
            spaceIndex.append(index)
        index += 1
    result.append(result[0])
    result.pop(0)
    for j in range(0, len(spaceIndex)):
        result.insert(spaceIndex[j], ' ')
    return ''.join(result)
