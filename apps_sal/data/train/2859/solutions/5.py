def largest_sum(arr):

    largest = 0
    temp = 0

    for num in arr:
        temp += num
        if temp < 0:
            temp = 0
        elif temp > largest:
            largest = temp

    return largest
