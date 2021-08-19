def repeats(arr):
    single = []  # create a list to store single numbers
    for i in arr:  # loop thru the array
        if arr.count(i) == 1:  # if a number occurs more than once in the array
            single.append(i)  # attach it to the singles list
    total = sum(single)
    return total
