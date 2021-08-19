def sum_mix(arr):

    # start with a running total of zero
    total = 0

    # first convert all to int form
    # then add to running total
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        total = total + arr[i]

    return(total)

    # your code here
