def check_exam(arr1,arr2):
    result = 0
    for i in range(len(arr1)):
        if arr2[i] == '':
            result += 0
        elif arr1[i] == arr2[i]:
            result += 4
        elif arr1[i] != arr2[i]:
            result -= 1
    return 0 if result < 0 else result
  

