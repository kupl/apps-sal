def check_exam(arr1, arr2):
    print((arr1, arr2))
    i = 0
    result = []
    while i < len(arr1):
        if arr1[i] == arr2[i]:
            result.append(4)
        elif arr2[i] == "":
            result.append(0)
        else:
            result.append(-1)
        i += 1
    return sum(result) if sum(result) > 0 else 0
