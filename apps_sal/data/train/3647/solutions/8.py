def solve(arr):

    # sort and reverse the list, make a new list to store answer
    arr = sorted(arr, reverse=True)
    new_list = []

    boolean = True
    # while there are still items in arr[]
    while (len(arr) >= 1):

        # append the 0th item to new_list[]
        new_list.append(arr[0])

        # flip our boolean value from true to false to reverse the list later
        if (boolean == True):
            boolean = False
        else:
            boolean = True

        # remove the 0th element from arr[]
        arr.pop(0)

        # sort the list either forwards or in reverse based on boolean
        arr = sorted(arr, reverse=boolean)

    return new_list
