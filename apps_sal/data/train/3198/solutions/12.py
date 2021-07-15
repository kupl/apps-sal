def check_anwser(actual, expected):
    if not actual:
        return 0
    return 4 if actual == expected else -1

def check_exam(arr1,arr2):
    return max(0, sum(map(check_anwser, arr2, arr1)))


