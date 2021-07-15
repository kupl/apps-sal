def circularly_sorted(arr):
    flag= 0
    for i in range(0, len(arr)):
        prev = arr[i-1]
        if prev > arr[i]:
            flag +=1
    if flag > 1:
        return False
    else:
        return True
