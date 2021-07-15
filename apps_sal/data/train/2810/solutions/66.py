def solve(arr):
    result = []
    count = 0
    for el in arr:
        for i in range(len(el)):
            if i + 1 == ord(el[i].lower()) - 96:
                count += 1
        result.append(count)
        count = 0
    return result
