def letter_check(arr): 
    return all(c in arr[0].lower() for c in arr[1].lower())
