def check_exam(arr1, arr2):
    exam_score = 0
    for index in range(0, len(arr1)):
        if arr1[index] == arr2[index]:
            exam_score += 4
        elif arr1[index] != arr2[index]:
            if arr2[index] == '':
                exam_score += 0
            else:
                exam_score -= 1
    if exam_score < 0:
        return 0
    else:
        return exam_score
