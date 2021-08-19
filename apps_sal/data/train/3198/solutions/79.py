def check_exam(arr1, arr2):
    marks_count = 0
    for i in range(0, len(arr2)):
        if arr2[i] == '':
            marks_count += 0
        elif arr2[i] == arr1[i]:
            marks_count += 4
        elif arr2[i] != arr1[i]:
            marks_count -= 1
    if marks_count < 0:
        return 0
    else:
        return marks_count
