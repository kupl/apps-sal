def sequence_classifier(arr):
    if len(set(arr)) == 1:
        return 5
    elif sorted(arr) == arr and len(arr) == len(set(arr)):
        return 1
    elif sorted(arr) == arr:
        return 2
    elif sorted(arr[::-1]) == arr[::-1] and len(arr) == len(set(arr)):
        return 3
    elif sorted(arr[::-1]) == arr[::-1]:
        return 4
    else:
        return 0
