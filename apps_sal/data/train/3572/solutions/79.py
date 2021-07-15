def invite_more_women(arr):
    sum = 0
    for element in arr:
        sum += element
    if sum > 0:
        return True
    elif sum <= 0:
        return False
