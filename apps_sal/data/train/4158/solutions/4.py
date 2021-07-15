def letter_check(arr): 
    for i in (list(set(arr[1].lower()))):
        if i not in arr[0].lower():
            return False
    return True
