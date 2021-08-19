def sum_array(arr):
    # your code here
    sum = 0
    if arr == None or arr == []:
        return 0

    else:
        new = sorted(arr)

    for i in range(1, len(new) - 1):
        sum += new[i]

    return sum
