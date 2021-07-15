def check_exam(arr1,arr2):
    corr = 0
    blank = 0
    for n in range(4):
        if arr2[n] == arr1[n] and arr2[n] != "":
            corr += 1
        elif arr2[n] == "":
            blank += 1
    return (4*corr - (4-corr-blank)) if (4*corr - (4-corr-blank)) > 0 else 0
  

