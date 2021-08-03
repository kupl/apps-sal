def check_exam(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2):
        if a == b:
            result.append(4)
        elif len(a) != len(b):
            result.append(0)
        elif a != b:
            result.append(-1)

    score = sum(result)
    if score < 0:
        return 0
    else:
        return score
