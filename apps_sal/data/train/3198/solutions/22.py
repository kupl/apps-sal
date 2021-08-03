def check_exam(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        if arr2[i] == "":
            result.append(0)
        elif arr1[i] == arr2[i]:
            result.append(4)
        else:
            result.append(-1)

    return sum(result) if sum(result) > 0 else 0
