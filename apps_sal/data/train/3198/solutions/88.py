def check_exam(arr1,arr2):
    count = 0
    for i in range(len(arr1)):
        if arr2[i] == "":
            count += 0
        elif arr1[i]==arr2[i]:
            count += 4
        elif arr1[i]!=arr2[i]:
            count -= 1
    return 0 if count<0 else count
  

