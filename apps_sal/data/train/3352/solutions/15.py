def find_longest(arr):
    largest = 0
    for i in range(len(arr)):
        a = arr[i] / 10
        x = 1
        while a > 1:
            a = a / 10
            x += 1
        if x > largest:
            largest = x
            largestVal = arr[i]
    return largestVal
