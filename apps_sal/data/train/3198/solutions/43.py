def check_exam(arr1, arr2):
    sum = 0
    i = 0
    while(i < len(arr1)):
        if(arr1[i] == arr2[i]):
            sum = sum + 4
            i = i + 1
            continue
        elif(arr2[i] == ""):
            sum = sum
            i = i + 1
            continue
        else:
            sum = sum - 1
            i = i + 1
    if(sum < 0):
        sum = 0
        return sum
    else:
        return sum
