def product(numbers):
    if numbers == None:
        return None
    elif numbers == []:
        return None

    pr = 1
    for i in numbers:
        pr *= i
    return pr
