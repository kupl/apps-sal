def check_exam(arr1, arr2):
    points = 0
    for a, b in zip(arr1, arr2):
        if a == b:
            points += 4
        elif b and 1 != b:
            points -= 1
    return points if points > 0 else 0
