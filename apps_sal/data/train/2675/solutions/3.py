def bad_apples(apples):
    free = None
    i = 0
    while i < len(apples):
        if 0 in apples[i]:
            if set(apples[i]) == {0}:
                apples.pop(i)
            else:
                apples[i].remove(0)
                if free != None:
                    apples[free].append(apples[i][0])
                    apples.pop(i)
                    free = None
                else:
                    free = i
            i -= 1
        i += 1
    if free != None:
        apples.pop(free)
    return apples
