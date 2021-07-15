def find_longest(arr):
    mostDigits = arr[0]
    for i in range(1, len(arr)):
        if len(str(arr[i])) > len(str(mostDigits)):
            if arr[i] > mostDigits:
                mostDigits = arr[i]
    
    return mostDigits
