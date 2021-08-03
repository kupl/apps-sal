def minimum(arr):
    # your code here...
    numbers = arr

    numbers.sort()

    minimum_number = numbers[0]

    return minimum_number


def maximum(arr):
    #...and here
    numbers = arr

    numbers.sort()

    max_number = numbers[-1]

    return max_number
