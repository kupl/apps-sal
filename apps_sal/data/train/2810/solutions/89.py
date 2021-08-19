def solve(arr):
    cunt = []
    for fuck in arr:
        temp = 0
        for (index, cum) in enumerate(fuck):
            if ord(cum.lower()) - 96 == index + 1:
                temp += 1
        cunt.append(temp)
    return cunt
