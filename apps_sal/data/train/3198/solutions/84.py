def check_exam(arr1,arr2):
    grade = 0
    for answer in range(len(arr1)):
        if arr1[answer] == arr2[answer]:
            grade += 4
        elif arr2[answer] == '':
            grade += 0
        else:
            grade -= 1
    return 0 if grade < 0 else grade
