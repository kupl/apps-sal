def odd_or_even(arr):
    # calculate if sum is odd or even using modulus
    test = sum(arr[-(len(arr)):]) % 2
    # return value as string
    if test == 0:
        return "even"
    else:
        return "odd"
