def check_exam(arr1, arr2):
    total_grade = 0
    for i in range(max(len(arr1), len(arr2))):
        if arr2[i] == arr1[i]:
            total_grade += 4
        elif arr2[i] == "":
            total_grade += 0
        elif arr2[i] != arr1[i]:
            total_grade -= 1

    return max(total_grade, 0)
