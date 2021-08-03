def max_number(n):
    newList = [i for i in str(n)]
    maxList = []
    while len(newList) > 0:
        maxList.append(max(newList))
        newList.remove(max(newList))
    return int(''.join(maxList))
