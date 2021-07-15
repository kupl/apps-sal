def check_exam(arr1,arr2):
    result = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            result += 4
        elif arr2[i] == '':
            result += 0
        else:
            result -= 1
    if result > 0:
        return result
    else:
        return 0
  

