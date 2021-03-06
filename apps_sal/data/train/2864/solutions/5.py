def merge_arrays(a, b):
    result = []
    currA = 0
    currB = 0
    while currA < len(a) and currB < len(b):
        if a[currA] < b[currB]:
            if not result or result[-1] != a[currA]:
                result.append(a[currA])
            currA += 1
        elif b[currB] < a[currA]:
            if not result or result[-1] != b[currB]:
                result.append(b[currB])
            currB += 1
        else:
            val = a[currA]
            countA = 0
            while currA < len(a):
                if a[currA] == val:
                    countA += 1
                    currA += 1
                else:
                    break
            countB = 0
            while currB < len(b):
                if b[currB] == val:
                    countB += 1
                    currB += 1
                else:
                    break
            if countA == countB:
                result.append(val)
    while currA < len(a):
        if not result or result[-1] != a[currA]:
            result.append(a[currA])
        currA += 1
    while currB < len(b):
        if not result or result[-1] != b[currB]:
            result.append(b[currB])
        currB += 1
    return result
