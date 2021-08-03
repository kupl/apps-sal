def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):  # To cycle through the array.
        if arr2[i] == "":  # Blank answer
            score += 0
        elif arr2[i] == arr1[i]:  # Correct answer
            score += 4
        else:  # Wrong answer
            score -= 1

    if score < 0:  # To deal with negative scores.
        return 0
    else:
        return score
