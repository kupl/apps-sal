def letter_check(arr): 
    return not set(arr[1].lower()) - set(arr[0].lower())
