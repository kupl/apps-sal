def is_sorted_and_how(arr):
    # Check to see if the array is starting off ascending
    if arr[0] < arr[1]:
        # Loop through the array to see if any items break that ascending fashion
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # If they do, return no
                return 'no'
        # If we made it through all items and didn't return no, return yes ascending
        return 'yes, ascending'
    # Check to see if the array is starting off descending
    if arr[0] > arr[1]:
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                return 'no'
        return 'yes, descending'
