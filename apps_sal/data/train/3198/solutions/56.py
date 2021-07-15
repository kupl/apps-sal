def check_exam(arr1,arr2):
    finalmark=0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            finalmark+=4
        if arr1[i] != arr2[i] and arr2[i] != '':
            finalmark-=1
    if finalmark < 0:
        finalmark=0
    return finalmark
  

