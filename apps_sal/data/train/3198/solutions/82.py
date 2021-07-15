def check_exam(arr1,arr2):
    sum = 0
    for grade in range(len(arr1)):
        if  arr1[grade] == arr2[grade]:
            sum += 4
        elif arr2[grade] == "":
            sum += 0
        else:
            sum -= 1
    return sum if sum > 0 else 0
  

