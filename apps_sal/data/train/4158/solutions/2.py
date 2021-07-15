def letter_check(arr): 
    for i in arr[1]:
        if i.lower()not in arr[0].lower():
            return False
    return True
